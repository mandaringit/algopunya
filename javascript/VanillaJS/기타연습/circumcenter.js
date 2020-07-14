(function () {
    function r(e, n, t) {
        function o(i, f) {
            if (!n[i]) {
                if (!e[i]) {
                    var c = "function" == typeof require && require;
                    if (!f && c) return c(i, !0);
                    if (u) return u(i, !0);
                    var a = new Error("Cannot find module '" + i + "'");
                    throw a.code = "MODULE_NOT_FOUND", a
                }
                var p = n[i] = {
                    exports: {}
                };
                e[i][0].call(p.exports, function (r) {
                    var n = e[i][1][r];
                    return o(n || r)
                }, p, p.exports, r, e, n, t)
            }
            return n[i].exports
        }
        for (var u = "function" == typeof require && require, i = 0; i < t.length; i++) o(t[i]);
        return o
    }
    return r
})()({
    1: [function (require, module, exports) {
        var circumcenter = require("circumcenter")
        window.circumcenter = circumcenter

    }, {
        "circumcenter": 2
    }],
    2: [function (require, module, exports) {
        "use strict"

        var dup = require("dup")
        var solve = require("robust-linear-solve")

        function dot(a, b) {
            var s = 0.0
            var d = a.length
            for (var i = 0; i < d; ++i) {
                s += a[i] * b[i]
            }
            return s
        }

        function barycentricCircumcenter(points) {
            var N = points.length
            if (N === 0) {
                return []
            }

            var D = points[0].length
            var A = dup([points.length + 1, points.length + 1], 1.0)
            var b = dup([points.length + 1], 1.0)
            A[N][N] = 0.0
            for (var i = 0; i < N; ++i) {
                for (var j = 0; j <= i; ++j) {
                    A[j][i] = A[i][j] = 2.0 * dot(points[i], points[j])
                }
                b[i] = dot(points[i], points[i])
            }
            var x = solve(A, b)

            var denom = 0.0
            var h = x[N + 1]
            for (var i = 0; i < h.length; ++i) {
                denom += h[i]
            }

            var y = new Array(N)
            for (var i = 0; i < N; ++i) {
                var h = x[i]
                var numer = 0.0
                for (var j = 0; j < h.length; ++j) {
                    numer += h[j]
                }
                y[i] = numer / denom
            }

            return y
        }

        function circumcenter(points) {
            if (points.length === 0) {
                return []
            }
            var D = points[0].length
            var result = dup([D])
            var weights = barycentricCircumcenter(points)
            for (var i = 0; i < points.length; ++i) {
                for (var j = 0; j < D; ++j) {
                    result[j] += points[i][j] * weights[i]
                }
            }
            return result
        }

        circumcenter.barycenetric = barycentricCircumcenter
        module.exports = circumcenter
    }, {
        "dup": 3,
        "robust-linear-solve": 6
    }],
    3: [function (require, module, exports) {
        "use strict"

        function dupe_array(count, value, i) {
            var c = count[i] | 0
            if (c <= 0) {
                return []
            }
            var result = new Array(c),
                j
            if (i === count.length - 1) {
                for (j = 0; j < c; ++j) {
                    result[j] = value
                }
            } else {
                for (j = 0; j < c; ++j) {
                    result[j] = dupe_array(count, value, i + 1)
                }
            }
            return result
        }

        function dupe_number(count, value) {
            var result, i
            result = new Array(count)
            for (i = 0; i < count; ++i) {
                result[i] = value
            }
            return result
        }

        function dupe(count, value) {
            if (typeof value === "undefined") {
                value = 0
            }
            switch (typeof count) {
                case "number":
                    if (count > 0) {
                        return dupe_number(count | 0, value)
                    }
                    break
                case "object":
                    if (typeof (count.length) === "number") {
                        return dupe_array(count, value, 0)
                    }
                    break
            }
            return []
        }

        module.exports = dupe
    }, {}],
    4: [function (require, module, exports) {
        "use strict"

        module.exports = compressExpansion

        function compressExpansion(e) {
            var m = e.length
            var Q = e[e.length - 1]
            var bottom = m
            for (var i = m - 2; i >= 0; --i) {
                var a = Q
                var b = e[i]
                Q = a + b
                var bv = Q - a
                var q = b - bv
                if (q) {
                    e[--bottom] = Q
                    Q = q
                }
            }
            var top = 0
            for (var i = bottom; i < m; ++i) {
                var a = e[i]
                var b = Q
                Q = a + b
                var bv = Q - a
                var q = b - bv
                if (q) {
                    e[top++] = q
                }
            }
            e[top++] = Q
            e.length = top
            return e
        }
    }, {}],
    5: [function (require, module, exports) {
        "use strict"

        var twoProduct = require("two-product")
        var robustSum = require("robust-sum")
        var robustScale = require("robust-scale")
        var compress = require("robust-compress")

        var NUM_EXPANDED = 6

        function cofactor(m, c) {
            var result = new Array(m.length - 1)
            for (var i = 1; i < m.length; ++i) {
                var r = result[i - 1] = new Array(m.length - 1)
                for (var j = 0, k = 0; j < m.length; ++j) {
                    if (j === c) {
                        continue
                    }
                    r[k++] = m[i][j]
                }
            }
            return result
        }

        function matrix(n) {
            var result = new Array(n)
            for (var i = 0; i < n; ++i) {
                result[i] = new Array(n)
                for (var j = 0; j < n; ++j) {
                    result[i][j] = ["m[", i, "][", j, "]"].join("")
                }
            }
            return result
        }

        function sign(n) {
            if (n & 1) {
                return "-"
            }
            return ""
        }

        function generateSum(expr) {
            if (expr.length === 1) {
                return expr[0]
            } else if (expr.length === 2) {
                return ["sum(", expr[0], ",", expr[1], ")"].join("")
            } else {
                var m = expr.length >> 1
                return ["sum(", generateSum(expr.slice(0, m)), ",", generateSum(expr.slice(m)), ")"].join("")
            }
        }

        function determinant(m) {
            if (m.length === 2) {
                return ["sum(prod(", m[0][0], ",", m[1][1], "),prod(-", m[0][1], ",", m[1][0], "))"].join("")
            } else {
                var expr = []
                for (var i = 0; i < m.length; ++i) {
                    expr.push(["scale(", determinant(cofactor(m, i)), ",", sign(i), m[0][i], ")"].join(""))
                }
                return generateSum(expr)
            }
        }

        function compileDeterminant(n) {
            var proc = new Function("sum", "scale", "prod", "compress", [
                "function robustDeterminant", n, "(m){return compress(",
                determinant(matrix(n)),
                ")};return robustDeterminant", n
            ].join(""))
            return proc(robustSum, robustScale, twoProduct, compress)
        }

        var CACHE = [
            function robustDeterminant0() {
                return [0]
            },
            function robustDeterminant1(m) {
                return [m[0][0]]
            }
        ]

        function generateDispatch() {
            while (CACHE.length < NUM_EXPANDED) {
                CACHE.push(compileDeterminant(CACHE.length))
            }
            var procArgs = []
            var code = ["function robustDeterminant(m){switch(m.length){"]
            for (var i = 0; i < NUM_EXPANDED; ++i) {
                procArgs.push("det" + i)
                code.push("case ", i, ":return det", i, "(m);")
            }
            code.push("}\
    var det=CACHE[m.length];\
    if(!det)\
    det=CACHE[m.length]=gen(m.length);\
    return det(m);\
    }\
    return robustDeterminant")
            procArgs.push("CACHE", "gen", code.join(""))
            var proc = Function.apply(undefined, procArgs)
            module.exports = proc.apply(undefined, CACHE.concat([CACHE, compileDeterminant]))
            for (var i = 0; i < CACHE.length; ++i) {
                module.exports[i] = CACHE[i]
            }
        }

        generateDispatch()
    }, {
        "robust-compress": 4,
        "robust-scale": 7,
        "robust-sum": 8,
        "two-product": 9
    }],
    6: [function (require, module, exports) {
        "use strict"

        var determinant = require("robust-determinant")

        var NUM_EXPAND = 6

        function generateSolver(n) {
            var funcName = "robustLinearSolve" + n + "d"
            var code = ["function ", funcName, "(A,b){return ["]
            for (var i = 0; i < n; ++i) {
                code.push("det([")
                for (var j = 0; j < n; ++j) {
                    if (j > 0) {
                        code.push(",")
                    }
                    code.push("[")
                    for (var k = 0; k < n; ++k) {
                        if (k > 0) {
                            code.push(",")
                        }
                        if (k === i) {
                            code.push("+b[", j, "]")
                        } else {
                            code.push("+A[", j, "][", k, "]")
                        }
                    }
                    code.push("]")
                }
                code.push("]),")
            }
            code.push("det(A)]}return ", funcName)
            var proc = new Function("det", code.join(""))
            if (n < 6) {
                return proc(determinant[n])
            }
            return proc(determinant)
        }

        function robustLinearSolve0d() {
            return [0]
        }

        function robustLinearSolve1d(A, b) {
            return [
                [b[0]],
                [A[0][0]]
            ]
        }

        var CACHE = [
            robustLinearSolve0d,
            robustLinearSolve1d
        ]

        function generateDispatch() {
            while (CACHE.length < NUM_EXPAND) {
                CACHE.push(generateSolver(CACHE.length))
            }
            var procArgs = []
            var code = ["function dispatchLinearSolve(A,b){switch(A.length){"]
            for (var i = 0; i < NUM_EXPAND; ++i) {
                procArgs.push("s" + i)
                code.push("case ", i, ":return s", i, "(A,b);")
            }
            code.push("}var s=CACHE[A.length];if(!s)s=CACHE[A.length]=g(A.length);return s(A,b)}return dispatchLinearSolve")
            procArgs.push("CACHE", "g", code.join(""))
            var proc = Function.apply(undefined, procArgs)
            module.exports = proc.apply(undefined, CACHE.concat([CACHE, generateSolver]))
            for (var i = 0; i < NUM_EXPAND; ++i) {
                module.exports[i] = CACHE[i]
            }
        }

        generateDispatch()
    }, {
        "robust-determinant": 5
    }],
    7: [function (require, module, exports) {
        "use strict"

        var twoProduct = require("two-product")
        var twoSum = require("two-sum")

        module.exports = scaleLinearExpansion

        function scaleLinearExpansion(e, scale) {
            var n = e.length
            if (n === 1) {
                var ts = twoProduct(e[0], scale)
                if (ts[0]) {
                    return ts
                }
                return [ts[1]]
            }
            var g = new Array(2 * n)
            var q = [0.1, 0.1]
            var t = [0.1, 0.1]
            var count = 0
            twoProduct(e[0], scale, q)
            if (q[0]) {
                g[count++] = q[0]
            }
            for (var i = 1; i < n; ++i) {
                twoProduct(e[i], scale, t)
                var pq = q[1]
                twoSum(pq, t[0], q)
                if (q[0]) {
                    g[count++] = q[0]
                }
                var a = t[1]
                var b = q[1]
                var x = a + b
                var bv = x - a
                var y = b - bv
                q[1] = x
                if (y) {
                    g[count++] = y
                }
            }
            if (q[1]) {
                g[count++] = q[1]
            }
            if (count === 0) {
                g[count++] = 0.0
            }
            g.length = count
            return g
        }
    }, {
        "two-product": 9,
        "two-sum": 10
    }],
    8: [function (require, module, exports) {
        "use strict"

        module.exports = linearExpansionSum

        //Easy case: Add two scalars
        function scalarScalar(a, b) {
            var x = a + b
            var bv = x - a
            var av = x - bv
            var br = b - bv
            var ar = a - av
            var y = ar + br
            if (y) {
                return [y, x]
            }
            return [x]
        }

        function linearExpansionSum(e, f) {
            var ne = e.length | 0
            var nf = f.length | 0
            if (ne === 1 && nf === 1) {
                return scalarScalar(e[0], f[0])
            }
            var n = ne + nf
            var g = new Array(n)
            var count = 0
            var eptr = 0
            var fptr = 0
            var abs = Math.abs
            var ei = e[eptr]
            var ea = abs(ei)
            var fi = f[fptr]
            var fa = abs(fi)
            var a, b
            if (ea < fa) {
                b = ei
                eptr += 1
                if (eptr < ne) {
                    ei = e[eptr]
                    ea = abs(ei)
                }
            } else {
                b = fi
                fptr += 1
                if (fptr < nf) {
                    fi = f[fptr]
                    fa = abs(fi)
                }
            }
            if ((eptr < ne && ea < fa) || (fptr >= nf)) {
                a = ei
                eptr += 1
                if (eptr < ne) {
                    ei = e[eptr]
                    ea = abs(ei)
                }
            } else {
                a = fi
                fptr += 1
                if (fptr < nf) {
                    fi = f[fptr]
                    fa = abs(fi)
                }
            }
            var x = a + b
            var bv = x - a
            var y = b - bv
            var q0 = y
            var q1 = x
            var _x, _bv, _av, _br, _ar
            while (eptr < ne && fptr < nf) {
                if (ea < fa) {
                    a = ei
                    eptr += 1
                    if (eptr < ne) {
                        ei = e[eptr]
                        ea = abs(ei)
                    }
                } else {
                    a = fi
                    fptr += 1
                    if (fptr < nf) {
                        fi = f[fptr]
                        fa = abs(fi)
                    }
                }
                b = q0
                x = a + b
                bv = x - a
                y = b - bv
                if (y) {
                    g[count++] = y
                }
                _x = q1 + x
                _bv = _x - q1
                _av = _x - _bv
                _br = x - _bv
                _ar = q1 - _av
                q0 = _ar + _br
                q1 = _x
            }
            while (eptr < ne) {
                a = ei
                b = q0
                x = a + b
                bv = x - a
                y = b - bv
                if (y) {
                    g[count++] = y
                }
                _x = q1 + x
                _bv = _x - q1
                _av = _x - _bv
                _br = x - _bv
                _ar = q1 - _av
                q0 = _ar + _br
                q1 = _x
                eptr += 1
                if (eptr < ne) {
                    ei = e[eptr]
                }
            }
            while (fptr < nf) {
                a = fi
                b = q0
                x = a + b
                bv = x - a
                y = b - bv
                if (y) {
                    g[count++] = y
                }
                _x = q1 + x
                _bv = _x - q1
                _av = _x - _bv
                _br = x - _bv
                _ar = q1 - _av
                q0 = _ar + _br
                q1 = _x
                fptr += 1
                if (fptr < nf) {
                    fi = f[fptr]
                }
            }
            if (q0) {
                g[count++] = q0
            }
            if (q1) {
                g[count++] = q1
            }
            if (!count) {
                g[count++] = 0.0
            }
            g.length = count
            return g
        }
    }, {}],
    9: [function (require, module, exports) {
        "use strict"

        module.exports = twoProduct

        var SPLITTER = +(Math.pow(2, 27) + 1.0)

        function twoProduct(a, b, result) {
            var x = a * b

            var c = SPLITTER * a
            var abig = c - a
            var ahi = c - abig
            var alo = a - ahi

            var d = SPLITTER * b
            var bbig = d - b
            var bhi = d - bbig
            var blo = b - bhi

            var err1 = x - (ahi * bhi)
            var err2 = err1 - (alo * bhi)
            var err3 = err2 - (ahi * blo)

            var y = alo * blo - err3

            if (result) {
                result[0] = y
                result[1] = x
                return result
            }

            return [y, x]
        }
    }, {}],
    10: [function (require, module, exports) {
        "use strict"

        module.exports = fastTwoSum

        function fastTwoSum(a, b, result) {
            var x = a + b
            var bv = x - a
            var av = x - bv
            var br = b - bv
            var ar = a - av
            if (result) {
                result[0] = ar + br
                result[1] = x
                return result
            }
            return [ar + br, x]
        }
    }, {}]
}, {}, [1]);