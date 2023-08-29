// This is an implementation using built-in methods of working with arrays
export function longestPalindrome(str: string): string {
    // Init longest is the first char itself
    let max_palindrome_len = 1;
    let longest_palindrome = str[0];

    const m = str.length;

    for (let start_index = 0; start_index < m - max_palindrome_len; ++start_index) {
        let max_possible_len = m - start_index;

        for (let checking_len = max_possible_len; checking_len > max_palindrome_len; --checking_len) {
            let end_index = start_index - 1 + checking_len;

            let isPalin = true;
            for (let k = 0; k < checking_len / 2; ++k){
                if (str[start_index + k] !== str[end_index - k]){
                    isPalin = false;
                    break;
                }
            }

            if (!isPalin)
                continue; // Trying different length

            longest_palindrome = str.substring(start_index, end_index + 1);
            max_palindrome_len = longest_palindrome.length;

            break; // We don't need to check shorter length
        }
    }

    return longest_palindrome;
};

// Score: 52% CPU + 99% RAM