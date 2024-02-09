import sys
import random
import pandas as pd
from tqdm import trange
from time import sleep

# Read CSV files (ADDED)
candidates = pd.read_csv('data/processed_candidates.csv')
jobs = pd.read_csv('data/processed_jobs.csv')

# Compute the preference matrix for the given dataframes
def compute_preference_matrix(candidates, jobs):
    # use jobs and candidates indices instead of fullname and company as it guarantees uniqueness
    jobs_indices = [i for i in range(len(jobs))]
    candidate_indices = [i for i in range(len(candidates))]

    # create the compatibility dataframe/matrix
    compatibility = pd.DataFrame(0, index=candidate_indices, columns=jobs_indices)
    compatibility = compatibility.rename_axis(index='Candidate IDs', columns='Job IDs')

    # populate the compatibility matrix
    print("Populating the Compatibility matrix...")
    populate_compatibility_matrix(compatibility, candidates, jobs)
    print("Population operation completed.")

    return compatibility

# Populate the compatibility matrix using the jobs and candidates dataframe
def populate_compatibility_matrix(matrix, candidates, jobs):
    for i in trange(len(candidates), file=sys.stdout, colour='GREEN'):
        for j in range(len(jobs)):
            matrix.loc[(i, j)] = compute_compatibility(candidates.loc[i], jobs.loc[j])
        sleep(0)

# Return a score to classify the compatibility of a candidate to a job
def compute_compatibility(candidate, job):
    compatibility_score = 0

    # Check if student has similar experience
    if candidate["Experience"] == job["Field"]:
        compatibility_score += 1
    else:
        compatibility_score += 0.5

    # Assign a reduced factor based on how far off the MinScore the candidate's score is
    candidate_score = candidate["Score"]
    job_minscore = job["MinScore"]

    # Candidate will prefer job whose MinScore is closer to their achieved grade
    if candidate_score <= 0.9 * job_minscore or candidate_score >= 1.1 * job_minscore:
        compatibility_score += 1
    elif candidate_score <= 0.75 * job_minscore or candidate_score >= 1.25 * job_minscore:
        compatibility_score += 0.5
    else:
        compatibility_score += 0.25

    # Account for a candidate preferring location, pay, company title etc.
    compatibility_score += random.random()

    return round(compatibility_score, 2)

    
    