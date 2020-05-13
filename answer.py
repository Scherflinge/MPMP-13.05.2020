# Description:
# This file solves Matt Parker's Math's Problem for 13/05/2020
# The methodology of this solution comes from solving the problem backwards,
# looking for the value that would happen on the second to last day

import math
import time
PHI = (1+math.sqrt(5))/2


def DecayEq(a, n):
    # Description:
    # Based on the final value, what will the value be 'n' days before
    # the final value is reached, as predicted by the function a/(phi**n)
    return a/(PHI**n)


def revFib(finalday, secfinalday):
    # Description:
    # Based on the last 2 values, work backwards to find the numbers that
    # created the sequence
    thrfinalday = finalday - secfinalday

    # in the case that 0 was entered for the prevday, which would be
    # an illegal just send back the 2 days
    if thrfinalday > secfinalday:
        return[finalday, secfinalday]

    thisSequence = [finalday, secfinalday, thrfinalday]

    diff = thisSequence[-2]-thisSequence[-1]
    while(diff < thisSequence[-1]):
        thisSequence.append(diff)
        diff = thisSequence[-2]-thisSequence[-1]
    return thisSequence


def iterativeSearch(finVal):
    maxSeq = []
    # We know we only have to search above half the value
    # because two values below half the final value can
    # never add to equal the final value
    for lastDay in range(int(finVal/2), finVal-1):
        resultingsequence = revFib(finVal, lastDay)
        # if a longer sequence is found, take the longer sequence
        if len(resultingsequence) > len(maxSeq):
            maxSeq = resultingsequence
        # if 2 sequences have the same length, take the one that
        # has the lower starting value
        elif len(resultingsequence) == len(maxSeq):
            if resultingsequence[-1] < maxSeq[-1]:
                maxSeq = resultingsequence
    return maxSeq


def smartSearch(finVal):
    # Description:
    # This search looks at the values around the value finVal/PHI
    maxSeq = []
    possibleVal = int(finVal/PHI)
    searchRange = 10
    # As finVal gets larger, the second-to-last term can be more accurately
    # modeled by finVal/PHI.
    # For smaller values, it can end up being off,
    # so we add a search range to our upper and lower bounds.
    for lastDay in range(int(possibleVal-searchRange), int(possibleVal+searchRange)):
        resultingsequence = revFib(finVal, lastDay)
        # if a longer sequence is found, take the longer sequence
        if len(resultingsequence) > len(maxSeq):
            maxSeq = resultingsequence
        # if 2 sequences have the same length, take the one that
        # has the lower starting value
        elif len(resultingsequence) == len(maxSeq):
            if resultingsequence[-1] < maxSeq[-1]:
                maxSeq = resultingsequence
    return maxSeq


if __name__ == "__main__":
    finalEnd = int(input("Enter the final value: "))
    # We can try 2 approaches, a broad iterative search and a smarter search
    startTime = time.time()
    iterResult = iterativeSearch(finalEnd)
    endTime = time.time()
    print("Iterative search found in {0:.2f} secs".format(endTime-startTime))
    print(iterResult)

    startTime = time.time()
    smartResult = smartSearch(finalEnd)
    endTime = time.time()
    print("Smart search found in {0:.2f} secs".format(endTime-startTime))
    print(smartResult)

    seq = smartResult

    print("The two starting values are {0} and {1} and it takes {2} days to get to {3}".format(
        seq[-1], seq[-2]-seq[-1], len(seq), finalEnd))
    
    # We will check how well it fits the curve
    fit = 0
    for i in range(len(seq)):
        actualValue = DecayEq(finalEnd, i)
        foundValue = seq[i]
        fit += (actualValue-foundValue)/actualValue
    fit /= len(seq)
    print("How well does this fit the curve {0}/(phi^x)?".format(finalEnd))
    print("{0:.2f}%".format((1-fit)*100))
