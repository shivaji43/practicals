# Define a class to represent a job
class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

# Function to perform job sequencing with deadlines using a greedy method
def job_sequencing_with_deadlines(jobs):
    # Sort jobs in decreasing order of profit
    jobs.sort(key=lambda x: x.profit, reverse=True)

    # Find the maximum deadline among all jobs to create a slot array
    max_deadline = max(job.deadline for job in jobs)
    slot = [-1] * max_deadline  # Initialize all slots as free

    total_profit = 0
    job_sequence = []

    # Iterate over each job
    for job in jobs:
        # Find a free slot for this job, from the latest possible slot before its deadline
        for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slot[j] == -1:
                # Assign this job to the current slot
                slot[j] = job.job_id
                total_profit += job.profit
                job_sequence.append(job.job_id)
                break

    return job_sequence, total_profit

# Driver code
if __name__ == "__main__":
    try:
        # Get the number of jobs from the user
        num_jobs = int(input("Enter the number of jobs: "))

        # Create an empty list to store jobs
        jobs = []

        # Get job details from the user
        for i in range(num_jobs):
            job_id = input(f"Enter job ID for job {i + 1}: ")
            deadline = int(input(f"Enter deadline for job {job_id}: "))
            profit = int(input(f"Enter profit for job {job_id}: "))
            jobs.append(Job(job_id, deadline, profit))

        # Call the function to generate the job sequence
        job_sequence, total_profit = job_sequencing_with_deadlines(jobs)

        # Display results
        print("Jobs scheduled:", job_sequence)
        print("Total profit:", total_profit)

    except ValueError:
        print("Invalid input. Please enter valid integers for deadlines and profits.")
