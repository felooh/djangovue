<template>
  <div class="container">
    <form @submit="createStudent">
      <div class="form-row">
        <div class="col-md-4 mb-3">
          <label for="validationDefaultUsername">Name</label>
          <div class="input-group">
            <div class="input-group-prepend">
              <span class="input-group-text" id="inputGroupPrepend2">@</span>
            </div>
            <input v-model="student.name" type="text" class="form-control" id="validationDefaultUsername" placeholder="Username" aria-describedby="inputGroupPrepend2" required>
          </div>
        </div>
      </div>
      <div class="col-md-4 mb-3">
        <label for="validationDefault01">Course</label>
        <input v-model="student.course" type="text" class="form-control" id="validationDefault01" placeholder="Course" required>
      </div>
      <div class="col-md-4 mb-3">
        <label for="validationDefault02">Rating</label>
        <input v-model="student.rating" type="text" class="form-control" id="validationDefault02" placeholder="Rating" required>
      </div>
      <button class="btn btn-primary" type="submit">Submit form</button>
  
      </form>
  </div>
  
  <div class="container">
   
    <table class="table">
      <thead>
        <tr>
          <th scope="col">ID</th>
          <th scope="col">Name</th>
          <th scope="col">Course</th>
          <th scope="col">Rating</th>
        </tr>
      </thead>
      <tbody>
        
        <tr v-for="student in students" :key="student.id" @dblclick="editStudent(student)">
          <td>{{ student.id }}</td>
          <td v-if="!student.editing">{{ student.name }}</td>
          <td v-else><input v-model="student.name" type="text" class="form-control" @keyup.enter="saveStudent(student)" @blur="saveStudent(student)"></td>
          <td v-if="!student.editing">{{ student.course }}</td>
          <td v-else><input v-model="student.course" type="text" class="form-control" @keyup.enter="saveStudent(student)" @blur="saveStudent(student)"></td>
          <td v-if="!student.editing">{{ student.rating }}</td>
          <td v-else><input v-model="student.rating" type="text" class="form-control" @keyup.enter="saveStudent(student)" @blur="saveStudent(student)"></td>
          <td>
            <button class="btn btn-danger btn-sm" @click="deleteStudent(student.id)">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

</template>

<script>

export default {
  name: 'App',
  data(){
    return{
      student:{
        name:"",
        course:"",
        rating:""
      },

      students:[],

     }
  },
  async created(){

    var response = await fetch('http://localhost:8000/api/students/');
    this.students = await response.json();

  },
  methods:{
    async createStudent(){
      var response = await fetch('http://localhost:8000/api/students/',{
        method:"post",
        headers:{
          'Content-Type':'application/json'
        },
        body: JSON.stringify(this.student)
      })
      this.students.push(await response.json());
    },

    editStudent(student) {
      student.editing = true;
    },

    async saveStudent(student) {
      student.editing = false;
      try {
        await fetch(`http://localhost:8000/api/students/${student.id}/`, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(student),
        });
      } catch (error) {
        console.error('Error updating student:', error);
      }
    },
    
    async deleteStudent(studentId) {
      try {
        await fetch(`http://localhost:8000/api/students/${studentId}/`, {
          method: 'DELETE',
        });
        this.students = this.students.filter(student => student.id !== studentId);
      } catch (error) {
        console.error('Error deleting student:', error);
      }
    },
  }
}
  

  
  

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
