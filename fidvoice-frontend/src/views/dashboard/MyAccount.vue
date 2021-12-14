<template>
    <div class="page-my-account">
        <h1 class="title">My Account</h1>

        <button @click="processLogout" class="button">log out</button>
    </div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'MyAccount',
    methods: {
        processLogout() {
            let token = localStorage.getItem('token')
            axios.defaults.headers.common['Authorization'] = "Token " + token
            axios 
            .post('/fidvoice/api/token/logout/')
            .then(response => {
                axios.defaults.headers.common['Authorization'] = ""

                localStorage.removeItem("token")

                this.$store.commit('removeToken')

                this.$router.push('/')
            })
            
        }
    }
}
</script>