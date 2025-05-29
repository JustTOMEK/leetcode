function createHelloWorld() {
    return function () {
        var args = [];
        for (var _i = 0; _i < arguments.length; _i++) {
            args[_i] = arguments[_i];
        }
        return "Hello World";
    };
}
;
/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */ 
