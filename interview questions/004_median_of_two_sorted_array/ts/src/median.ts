// This is an implementation using built-in methods of working with arrays
export function findMedianSortedArrays1(nums1: number[], nums2: number[]): number {
    const m = nums1.length;
    const n = nums2.length;

    const arr = nums1.concat(nums2).sort(function(a,b){return a-b});
    console.log(arr)
    const len = arr.length;

    const isEven = len % 2 == 0;

    if(isEven)
        return (arr[len / 2 - 1] + arr[len / 2]) / 2;

    return arr[Math.floor(len / 2)];
};

// The final solution that beat %99 of submitted solutions
export function findMedianSortedArrays2(nums1: number[], nums2: number[]): number {
    const len = nums1.length + nums2.length;

    let arr: number[] = [];

    for (let i = 0; i < len; ++i) {
        let iEnd1 = nums1.length - 1
        let iEnd2 = nums2.length - 1

        let e1 = nums1[iEnd1];
        let e2 = nums2[iEnd2];

        if(iEnd1 >= 0 && (e1 >= e2 || e2 === undefined))
        {
            arr.push(e1);
            nums1.pop();
        }

        if (iEnd2 >= 0 && (e2 >= e1 || e1 === undefined))
        {
            arr.push(e2);
            nums2.pop();
        }
    }

    const isEven = len % 2 == 0;
    if(isEven)
        return (arr[len / 2 - 1] + arr[len / 2]) / 2;

    return arr[Math.floor(len / 2)];
};