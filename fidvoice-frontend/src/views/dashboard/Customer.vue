<template>
  <div class="columns is-multiline">
      <div column is-12>
          <h1 class="title">Customers</h1>
      </div>

      <div class="column is-3 mt-4" v-for="customer in customers" :key="customer.id">
          <div class="box">
              <h4 class="is-size-4 mb-4"> {{customer.name}} </h4>
              <router-link :to="{name: 'CustomerDetail', params: {id: customer.id}}" class="button is-success">Details</router-link>
          </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'Customers',
    data(){
        return {
            customers: [],
        }
    },
    mounted() {
        this.collectCustomers()
    },
    methods: {
        collectCustomers(){
            let token = localStorage.getItem('token')
            axios.defaults.headers.common['Authorization'] = "Token " + token
            axios 
            .get('/fidvoice/api/clients/')
            .then (response => {
                for (let client = 0; client < response.data.length; client++) {
                    this.customers.push(response.data[client])
                    
                }
            })
        }
    }
}
</script>

<style>

</style>