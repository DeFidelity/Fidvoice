<template>
  <div class="customer-detail-page">
      <div class="columns is-multiline">
          <div class="col-12">
              <h4 class="title"> {{customer.name}} </h4>
          </div>
          <div class="column is-12">
                <h2 class="subtitle">Contact details</h2>

                <p><strong>{{ client.name }}</strong></p>
                
                <p v-if="customer.address1">FIrst address: {{ customer.address1 }}</p>
                <p v-if="customer.address2">Second address{{ customer.address2 }}</p>
                <p v-if="customer.zipcode || customer.place">Zipcode and Contact place: {{ customer.zipcode }} {{ customer.place }}</p>
                <p v-if="customer.country">Country: {{ customer.country }}</p>
            </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
S
export default {
    name: 'CustomerDetail',
    data(){
        return {
            customer: {}
        }
    },
    mounted(){
        this.getCustomer()
    },
    methods: {
        getCustomer(){
            const customerID = this.$route.params.id 

            let token = localStorage.getItem('token')
            axios.defaults.headers.common['Authorization'] = "Token " + token 

            axios
            .get(`/fidvoice/api/clients/${customerID}`)
            .then(response => {
                this.customer = response.data
            })
            .catch(error =>{
                console.log(JSON.stringify(error))
            })
        }
    }
}
</script>

<style>

</style>