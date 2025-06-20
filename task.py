from flask import Flask,jsonify,request
from flask_cors import CORS  # Import CORS
import mysql.connector
app= Flask(__name__)#instance
CORS(app)

def get_db_connection():# made connection
    return mysql.connector.connect(
        host="localhost",    
        user="root",         
        password="bholupie",  
        database="task_manager"
    )
@app.route('/tasks',methods=['GET']) 
def get_tasks(): 
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, title, description, status, due_date, created_at, updated_at from tasks")
    tasks = cursor.fetchall()
    return jsonify({"tasks": tasks})

#post api to insert values
@app.route('/tasks', methods=['POST'])
def add_task():
    data=request.json
    title = data.get("title")
    description = data.get("description")
    status = data.get("status", "pending")            
    due_date = data.get("due_date") 
    conn = get_db_connection()
    cursor = conn.cursor()
    sql= "insert into tasks (title, description, status, due_date) values(%s, %s, %s, %s)"
    values = (title, description, status, due_date)
    cursor.execute(sql, values)
    conn.commit()
    task_id = cursor.lastrowid 
    return jsonify({"message": "Task added successfully!"})

#to get id specified task
@app.route('/tasks/<int:task_id>',methods=['GET'])
def get_task_by_id(task_id):
    conn = get_db_connection()  
    cursor = conn.cursor(dictionary=True)  
    cursor.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))#single tuple
    task = cursor.fetchone() 
    query = "SELECT id,title, description, status, due_date from tasks  WHERE id = " + str(task_id)
    
    cursor.execute(query)
    for row in cursor:  # Iterate over the cursor (no fetchall or fetchone)
        return jsonify(row)


    if task:  
        return jsonify({"task": task})
    else:  
        return jsonify({"error": "task not found"}), 404

# to update task by id using put request
@app.route('/tasks', methods=['PUT'])
def update_task ():
    data=request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    task_id = data['id'] #extract values
    title = data['title']
    description = data['description']
    status= data['status']
    due_date = data['due_date']
    query ="UPDATE tasks SET title = %s,description = %s,status = %s,due_date = %s WHERE id = %s"
    values =  (title, description, status, due_date,task_id)
    cursor.execute(query, values)
    conn.commit()
    return jsonify({"message": "Task updated successfully"})


# to delete task by id using delete request
@app.route('/tasks/<task_id>', methods=['DELETE'])
def delete_by_id(task_id):
    conn=get_db_connection()
    cursor=conn.cursor()

    query="DELETE from tasks where id="+task_id
    cursor.execute(query)
    conn.commit()
    return jsonify({"message": "Task with ID " + task_id + " deleted successfully"})


# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)#Starts the Flask

