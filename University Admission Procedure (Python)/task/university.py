

if __name__ == "__main__":
    score1 = int(input())
    score2 = int(input())
    score3 = int(input())
    average = (score1 + score2 + score3) / 3
    print(f"{average}")
    if average >= 60:
        print("Congratulations, you are accepted!")
    else:
        print("We regret to inform you that we will not be able to offer you admission.")
