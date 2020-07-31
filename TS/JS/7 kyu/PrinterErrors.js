"use strict";
// Printers Erros - 7kyu
Object.defineProperty(exports, "__esModule", { value: true });
var G964 = /** @class */ (function () {
    function G964() {
    }
    G964.printerError = function (s) {
        var _a;
        return ((s.match(/[n-z]/g) == null ? 0 : (_a = s.match(/[n-z]/g)) === null || _a === void 0 ? void 0 : _a.length) +
            '/' +
            s.length);
    };
    return G964;
}());
exports.G964 = G964;
