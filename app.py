import timeit, random
from flask import Flask, render_template, request, session
from flask_session import Session
from linear_search import linear_search, linear_search_wrapper
from binary_search import binary_search, binary_search_wrapper
from ternary_search import ternary_search, ternary_search_wrapper
from exponential_search import exponential_search, exponential_search_wrapper
from interpolation_search import interpolation_search, interpolation_search_wrapper
from jump_search import jump_search, jump_search_wrapper

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():
    size = 100
    if 'dataset' not in session:
        data = sorted(range(1, size + 1))
        session['dataset'] = ", ".join(map(str, data))
        session['target'] = random.choice(data)
        session['size'] = size

    if request.method == "POST":
        if 'generate' in request.form:
            size = int(request.form.get('size'))
            data = sorted(range(1, size + 1))
            session['dataset'] = ", ".join(map(str, data))
            session['target'] = random.choice(data)
        elif 'search' in request.form:
            array_str = session['dataset']
            search_type = request.form.get("search_type")
            
            try:
                size = int(request.form.get("size")) 
                array = list(map(int, array_str.split(", ")))
                target = int(request.form.get("target"))
                low, high = 0, len(array) - 1

                if search_type == "linear":
                    execution_time = timeit.timeit("linear_search_wrapper(linear_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = linear_search_wrapper(linear_search, array, target)  
                elif search_type == "binary":
                    execution_time = timeit.timeit("binary_search_wrapper(binary_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = binary_search_wrapper(binary_search, array, target)
                elif search_type == "ternary":
                    execution_time = timeit.timeit("ternary_search_wrapper(ternary_search, array, target, low, high)", globals={**globals(), "array": array, "target": target,"low":low,"high":high}, number=1)  * 1000 
                    result = ternary_search_wrapper(ternary_search, array, target, low, high)  
                elif search_type == "exponential":
                    execution_time = timeit.timeit("exponential_search_wrapper(exponential_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = exponential_search_wrapper(exponential_search, array, target)
                elif search_type == "interpolation":
                    execution_time = timeit.timeit("interpolation_search_wrapper(interpolation_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = interpolation_search_wrapper(interpolation_search, array, target) 
                elif search_type == "jump":
                    execution_time = timeit.timeit("jump_search_wrapper(jump_search, array, target)", globals={**globals(), "array": array, "target": target}, number=1)  * 1000 
                    result = jump_search_wrapper(jump_search, array, target)  

                return render_template("index.html", array=array, target=target, result=result, execution_time=execution_time, size=size, dataset=session['dataset'], search_type=search_type)
                
            except ValueError:
                return render_template("index.html", error="Invalid input. Ensure the array and target are integers.", dataset=session['dataset'], size=size, search_type=search_type)
        elif 'edit' in request.form:
            session['dataset'] = request.form.get('array')
        
    return render_template("index.html", dataset=session['dataset'], size=size, target=session['target'])

if __name__ == '__main__':
    app.secret_key = "secret"
    app.run(debug=True)
