<template>
  <div class="hello">
    <h1>{{ artistName }}</h1>
    <input type="text" v-model="artistName"/>
    <button type="button" v-on:click="getArtist">Search</button>
    <transition-group name="list" class="list-group">
      <span v-for="artist in relatedArtists" v-bind:key="artist" class="list-item">
        {{artist}}
      </span>
    </transition-group>
  </div>
</template>

<script>
  export default {
    name: 'hello',
    data: function () {
      return {
        artistName: '',
        relatedArtists: []
      }
    },
    methods: {
      getArtist: function () {
        fetch(`http://localhost:5000/artist?name=${this.$data.artistName}`)
          .then(response => response.json())
          .then(response => {
            this.getRelatedArtists(response.id)
          })
      },
      getRelatedArtists: function (artistId) {
        fetch(`http://localhost:5000/related?id=${artistId}`)
          .then(response => response.json())
          .then(response => {
            this.$data.relatedArtists = response.artists.map(artist => artist.name)
          })
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  .list-group {
    margin-top:10px;
    list-style-type: none;
    display: flex;
    flex-direction: column;
    padding: 0;
  }

  .list-item {
    display: inline-block;
    margin: 2px 0 2px 10px;
  }

  a {
    color: #42b983;
  }

  .list-enter-active, .list-leave-active {
    transition: all 1s;
  }
  .list-enter, .list-leave-to /* .list-leave-active below version 2.1.8 */ {
    opacity: 0;
    transform: translateY(30px);
  }
</style>
