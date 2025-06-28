// pre: sorted array of comparable elements
// post: index of the most similar word (close alphabeticaly)
export function bin_search<T>(el: T, vec: Array<T>): number {
    let start = 0;
    let end = vec.length - 1;

    while (start < end) {
        const middle = Math.floor((end + start) / 2);
        if (vec[middle] < el) {
            start = middle + 1;
        } else if (vec[middle] > el) {
            end = middle;
        } else {
            return middle;
        }
    }

    return start;
}

export function similarity(reference: string, word: string): number {
    let ptref = 0;
    let ptwrd = 0;
    let cont = true;
    let res = 0;

    while (ptref < reference.length && ptwrd < word.length) {
        if (reference[ptref] == word[ptwrd]) {
            if (cont) res += 100;
            else res += 1;
            ptref++;
            ptwrd++;
        } else {
            cont = false;
            ptwrd++;
        }
    }

    return res;
}
