function memoize(fn) {
    var dictionary = new Map;
    return function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        var key = args.join('.');
        if (dictionary.has(key)) {
            return dictionary.get(key);
        }
        var result = fn.apply(void 0, args);
        dictionary.set(key, result);
        return result;
    };
}
/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1
 */ 
