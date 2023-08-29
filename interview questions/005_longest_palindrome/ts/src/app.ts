import { longestPalindrome } from './palindrome';

class App {
    public static start() {
        //const str = 'babad';
        //const str = 'cbbd';
        const str = 'radarradarradar';

        const result = longestPalindrome(str);

        console.log(`Longest Palindrome = ${result}`);
    }
}

App.start();