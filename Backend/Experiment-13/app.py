from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Nish@2918#'
app.config['MYSQL_DB'] = 'student_db'

mysql = MySQL(app)

# ------------------ VALIDATION FUNCTION ------------------
def validate_student(data):
    if 'name' not in data or data['name'] == "":
        return "Name is required"
    if 'age' not in data or not isinstance(data['age'], int):
        return "Valid age is required"
    if 'email' not in data or '@' not in data['email']:
        return "Valid email required"
    return None

# ------------------ CREATE ------------------
@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()

    error = validate_student(data)
    if error:
        return jsonify({"error": error}), 400

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO student(name, age, email) VALUES(%s, %s, %s)",
                (data['name'], data['age'], data['email']))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Student added successfully"}), 201

# ------------------ READ ------------------
@app.route('/students', methods=['GET'])
def get_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    cur.close()

    result = []
    for row in rows:
        result.append({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "email": row[3]
        })

    return jsonify(result)

# ------------------ UPDATE ------------------
@app.route('/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()

    error = validate_student(data)
    if error:
        return jsonify({"error": error}), 400

    cur = mysql.connection.cursor()
    cur.execute("UPDATE student SET name=%s, age=%s, email=%s WHERE id=%s",
                (data['name'], data['age'], data['email'], id))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Student updated successfully"})

# ------------------ DELETE ------------------
@app.route('/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM student WHERE id=%s", (id,))
    mysql.connection.commit()
    cur.close()

    return jsonify({"message": "Student deleted successfully"})

# ------------------ RUN ------------------
if __name__ == '__main__':
    app.run(debug=True)