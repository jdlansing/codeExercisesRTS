class Exercises:
    def aboveBelow(self, numbers, compareNum):
        aboveBelowVal = {"above": 0, "below": 0}
        listSize = len(numbers)

        if (listSize > 0):
            numbers.sort()

            # First comparator. Since the list is sorted in ascending order, if the first number is greater
            # than the given value, then every subsequent value is, so there is no need to traverse the
            # entire list 
            if (numbers[0] > compareNum):
                aboveBelowVal["above"] = listSize
            # Likewise, if the last value is less than the given value, then so is every previous value,
            # so there is no need to traverse the whole list
            elif (numbers[listSize - 1] < compareNum):
                aboveBelowVal["below"] = listSize
            else:
                current = 0
                # We only need to check the values that are less than or equal to our given value, since
                # every other value after those will be greater, so simple math will give us the necessary
                # value for "above"
                while ((current != listSize) and (numbers[current] <= compareNum)):
                    # Filters out values that are equal to the given value, since we are only looking for
                    # values greater or lesser than
                    if (numbers[current] != compareNum):
                        aboveBelowVal["below"] += 1
                    current += 1
                aboveBelowVal["above"] = (listSize - current)

        return aboveBelowVal

    def stringRotation(self, original, amount):
        stringLength = len(original)

        if (stringLength != 0):
            # If amount is greater than the lenght of the string, then the string rotates around itself
            # multiple times, meaning the end result will appear to be the amount modded by the length of
            # the string
            modAmount = amount % stringLength

            # No need to do any string manipulation if the modded amount is 0, because if the string was rotated
            # around itself multiple times, the final string would just be identical to the original
            if (modAmount == 0):
                return original

            slicePoint = (stringLength - modAmount)
            frontSlice = original[:slicePoint]
            endSlice = original [slicePoint:]

            return (endSlice + frontSlice)
        
        return original