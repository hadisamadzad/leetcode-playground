import { findMedianSortedArrays1, findMedianSortedArrays2 } from './median';

class App {
    public static start() {
        const arr1 = [0,0];
        const arr2 = [0,0];

        const median = findMedianSortedArrays2(arr1, arr2);

        console.log(`Median = ${median}`);
    }
}

App.start();