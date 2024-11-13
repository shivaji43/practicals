class Job:
    def __init__(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing_with_deadlines(jobs):
    
    jobs.sort(key=lambda x: x.profit, reverse=True)

    
    max_deadline = max(job.deadline for job in jobs)
    slot = [-1] * max_deadline  

    total_profit = 0
    job_sequence = []

    
    for job in jobs:
        
        for j in range(min(max_deadline, job.deadline) - 1, -1, -1):
            if slot[j] == -1:
                
                slot[j] = job.job_id
                total_profit += job.profit
                job_sequence.append(job.job_id)
                break

    return job_sequence, total_profit


if __name__ == "__main__":
    try:
        
        num_jobs = int(input("Enter the number of jobs: "))

        
        jobs = []

       
        for i in range(num_jobs):
            job_id = input(f"Enter job ID for job {i + 1}: ")
            deadline = int(input(f"Enter deadline for job {job_id}: "))
            profit = int(input(f"Enter profit for job {job_id}: "))
            jobs.append(Job(job_id, deadline, profit))

        
        job_sequence, total_profit = job_sequencing_with_deadlines(jobs)

        
        print("Jobs scheduled:", job_sequence)
        print("Total profit:", total_profit)

    except ValueError:
        print("Invalid input. Please enter valid integers for deadlines and profits.")
