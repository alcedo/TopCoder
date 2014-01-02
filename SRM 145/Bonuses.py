# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect

class Bonuses:
    def getDivision(self, points):

        
        total_points = sum(points)

        def calc_percentage(x):
            return int(float(x)/float(total_points)*100) 

        def make_tuple(x,y):
            if type(x) is tuple:
                if type(y) is tuple:
                    return x + y

                return x + (y,)

            return (x,) + (y,)

        each_employee_percentage = [calc_percentage(x) for x in points]

        combined_data = zip(points, each_employee_percentage)
        print combined_data
        #left over percentages
        left_over = 100 - sum(each_employee_percentage)

        #find top x employees and their corresponding pt. 
        sorted_list = sorted(points, reverse=True)

        top_values = sorted_list[:left_over]

        seen = set()
        top_values = [x for x in top_values if x not in seen and not seen.add(x)]


        results = [] 
        for i in top_values:
            for j, item in enumerate(combined_data):
                if item[0] == i:
                    if left_over == 0:
                        break 
                    left_over = left_over -1
                    combined_data[j] = (item[0] ,  item[1] + 1 )
                    results.append( (item[0] ,  item[1] + 1 ))
                else: 
                    results.append( (item[0] ,  item[1]))

        results = [x[1] for x in combined_data]
        # results = [    for i in top_values for j in combined_data ]   
        print "--" 
        print sorted_list
        print top_values
        print combined_data
        print results 
        print "{ 8, 6, 4, 2, 8, 5, 5, 3, 1, 4, 5, 4, 6, 3, 5, 4, 1, 8, 1, 6, 3, 8 }"
        return tuple(results)

# CUT begin
# TEST CODE FOR PYTHON {{{
import sys, time, math

def tc_equal(expected, received):
    try:
        _t = type(expected)
        received = _t(received)
        if _t == list or _t == tuple:
            if len(expected) != len(received): return False
            return all(tc_equal(e, r) for (e, r) in zip(expected, received))
        elif _t == float:
            eps = 1e-9
            d = abs(received - expected)
            return not math.isnan(received) and not math.isnan(expected) and d <= eps * max(1.0, abs(expected))
        else:
            return expected == received
    except:
        return False

def pretty_str(x):
    if type(x) == str:
        return '"%s"' % x
    elif type(x) == tuple:
        return '(%s)' % (','.join( (pretty_str(y) for y in x) ) )
    else:
        return str(x)

def do_test(points, __expected):
    startTime = time.time()
    instance = Bonuses()
    exception = None
    try:
        __result = instance.getDivision(points);
    except:
        import traceback
        exception = traceback.format_exc()
    elapsed = time.time() - startTime   # in sec

    if exception is not None:
        sys.stdout.write("RUNTIME ERROR: \n")
        sys.stdout.write(exception + "\n")
        return 0

    if tc_equal(__expected, __result):
        sys.stdout.write("PASSED! " + ("(%.3f seconds)" % elapsed) + "\n")
        return 1
    else:
        sys.stdout.write("FAILED! " + ("(%.3f seconds)" % elapsed) + "\n")
        sys.stdout.write("           Expected: " + pretty_str(__expected) + "\n")
        sys.stdout.write("           Received: " + pretty_str(__result) + "\n")
        return 0

def run_tests():
    sys.stdout.write("Bonuses (250 Points)\n\n")

    passed = cases = 0
    case_set = set()
    for arg in sys.argv[1:]:
        case_set.add(int(arg))

    with open("Bonuses.sample", "r") as f:
        while True:
            label = f.readline()
            if not label.startswith("--"): break

            points = []
            for i in range(0, int(f.readline())):
                points.append(int(f.readline().rstrip()))
            points = tuple(points)
            f.readline()
            __answer = []
            for i in range(0, int(f.readline())):
                __answer.append(int(f.readline().rstrip()))
            __answer = tuple(__answer)

            cases += 1
            if len(case_set) > 0 and (cases - 1) in case_set: continue
            sys.stdout.write("  Testcase #%d ... " % (cases - 1))
            passed += do_test(points, __answer)

    sys.stdout.write("\nPassed : %d / %d cases\n" % (passed, cases))

    T = time.time() - 1387806927
    PT, TT = (T / 60.0, 75.0)
    points = 250 * (0.3 + (0.7 * TT * TT) / (10.0 * PT * PT + TT * TT))
    sys.stdout.write("Time   : %d minutes %d secs\n" % (int(T/60), T%60))
    sys.stdout.write("Score  : %.2f points\n" % points)

if __name__ == '__main__':
    run_tests()

# }}}
# CUT end
