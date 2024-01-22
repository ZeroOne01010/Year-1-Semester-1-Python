


#function to display list of candidates
def candidate_list(candidates):
    print("\nList of Candidates:")
    for i, candidate in enumerate(candidates, start=1):
        print(f"{i}. {candidate}")

#funtion to add votes and save to a variable
def vote(candidate_votes, candidate_index):
    candidate_votes[candidate_index] += 1

#function for print statement
def main():
    candidates = ["Candidate 1", "Candidate 2", "Candidate 3", "Candidate 4", "Candidate 5"]
    candidate_votes = [0] * len(candidates)

    print("Please enter the candidate number to vote (1-5), or enter -1 to quit the programme.")

    #While loop within the fucntion keeps asking for input until -1 is entered to end the programme
    while True:
        candidate_list(candidates)
        vote_selection = input("Please enter your vote: ")

        #exception handling and return error if any outside of -1 or 1 - 5 entered
        try:
            vote_number = int(vote_selection)
            if vote_number == -1:
                break
            elif 1 <= vote_number <= len(candidates):
                vote(candidate_votes, vote_number - 1)
            else:
                print("Invalid choice. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    print("\nVoting has ended. Results:")

     # sort the candidates in order of number of votes
    sorted_candidates = [candidate for _, candidate in sorted(zip(candidate_votes, candidates), reverse=True)]

    for i, candidate in enumerate(sorted_candidates, start=1):
        print(f"{i}. {candidate} - {candidate_votes[candidates.index(candidate)]} votes")

if __name__ == "__main__":
    main()