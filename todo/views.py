from django.http import HttpResponse

def task_create(request):
    html_response = """
        <style>
        h1 {
            color: #fff;
            width: 70%;
            text-align: center;
            background-color: blue;
            padding: 10px 0;
            
        }
        </style>
        <h1>Task Create Page</h1>
        <br> <br>
        <style>
        form {
            display: flex;
            flex-direction: column;
            width: 70%;
            color: #555;
              
        }
        
        label {
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        input, textarea, select, button {
            margin-bottom: 15px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        
        button:hover {
                cursor: pointer;
                background-color: #555;
                color: #fff;
        }
        </style>
        <form>
            <label for="task-name">Task name:</label>
            <input type="text" id="task-name">

            <br> <br>
            
            <label for="description">Description:</label>
            <textarea id="description" >
            </textarea>
            <br> <br>
            
            <label for="deadline">Deadline:</label>
            <input type="date" id="deadline" required>

            <br> <br>
            
            <label for="importance-level">Importance level:</label>
            <select id="importance-level" required>
                <option value="low">Low</option>
                <option value="medium">Medium</option>
                <option value="high">High</option>
            </select>
            </label>
            <br> <br>
             
            <button type="submit">Save the Task</button>
        
        
        </form>
        
    """
    return HttpResponse(html_response)
