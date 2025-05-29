function createCounter(n) {
    return function () {
        return n++;
    };
}
var counter = createCounter(10);
counter(); // 10
counter(); // 11
counter(); // 12
