package main

// longestPalindrome:
//   Returns the longest palindrome in string s.
func longestPalindrome(s string) (string) {
    r, strLen, windowSize := []rune(s), len(s), len(s)                      // r: rune of string s. windowSizeL length of string s.

    // Insert into r, the reverse of s.
    for i, j := 0, strLen-1; i < strLen/2; i, j = i+1, j-1 {                // Iterate from i increasing to midpoint, j decreasing to midpoint.
        r[i], r[j] = r[j], r[i]                                             // Assign r in opposite order of string s.
    }

    reversed := string(r)                                                   // Reverse of given string s.

    // Go through all window sizes and all possible strings in windows.
    // Check in order of largest to smallest window size.
    for windowSize > -1 {                                                   // Loop through valid window sizes.
        for i, j := 0, strLen-1; i < strLen-windowSize; i, j = i+1, j-1 {   // Loop through possible strings within window size.
            if s[i: i+windowSize+1] == reversed[j-windowSize: j+1] {        // If the current string in window is a palindrome.
                return s[i: i+windowSize+1]                                 // Return it.
            }
        }

        windowSize--                                                        // Decrease window size for next iteration.
    }

    return ""                                                               // Return default string: "".
}
