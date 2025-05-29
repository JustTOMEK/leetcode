function filter(arr, fn) {
    var filtered_arr = [];
    for (var i = 0; i < arr.length; i++) {
        if (fn(arr[i], i)) {
            filtered_arr.push(arr[i]);
        }
    }
    return;
}
;
