<template>
  <div class="page-login">
      <div class="columns">
        <div class="column is-4 is-offset-4">
            <h1 class="title">Login to your account</h1>
            
            <form @submit.prevent="processLogin">
                  <div class="field">
                      <label for="email">Username</label>
                      <div class="control">
                          <input type="text" name="email" class="input" v-model="username">
                      </div>
                  </div>

                  <div class="field">
                      <label for="password">Password</label>
                      <div class="control">
                          <input type="password" name="password" class="input" v-model="password">
                      </div>
                  </div>

                  <div class="notification is-danger" v-if="errors.length">
                      <p v-for="error in errors" :key="error">
                          {{ error }}
                      </p>
                  </div>

                  <div class="field">
                      <div class="control">
                          <button class="button is-success">Login</button>
                      </div>
                  </div>

              </form>
            
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Login',
    data(){
        return{
            username: '',
            password: '',
            email: '',
            errors: [],

        }
    },
    methods: {
        processLogin(e){
            axios.defaults.headers.common['Authorization'] = ""
            localStorage.removeItem["token"]

            const formData = {
                username: this.username,
                password: this.password
            }
            axios 
            .post('fidvoice/api/token/login/', formData)
            
            .then(response => {
                const token =response.data.auth_token 

                this.$store.commit('setToken', token)

                axios.defaults.headers.common['Authorization'] = "Token " + token

                localStorage.setItem("token", token)
                
                this.$router.push('/dashboard')
                })
        }
    }

}
</script>

<style>

</style>