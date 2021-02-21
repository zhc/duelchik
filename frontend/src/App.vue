<template>
  <div class="arena">
    <div class="players">
      <div v-for="ind in size">
        <div class="position" :class="{ 'player' : isYourPos(ind), 'enemy' : isEnemyPos(ind) }" @click="move(ind)"></div>
      </div>
    </div>
    <div class="cards">
      <div class="cards_inner">
        <div class="card" v-for="item in deck">{{ item }}</div>
      </div>
    </div>
  </div>
</template>
<script>
import store from "../src/store";

export default {
  data() {
    return {}
  },
  computed: {
    deck: function () {
      return store.getters.deck;
    },
    size: function () {
      return store.getters.size;
    },
  },
  created() {},
  methods: {
    move: function (ind) {
      store.dispatch('getMessage', ind);
    },
    isYourPos: function (ind) {
      return ind === store.getters.playerIndex;
    },
    isEnemyPos: function (ind) {
      return ind === store.getters.enemyIndex;
    }
  }
}
</script>
<style lang="scss">
.arena {

}

.players {
  display: flex;
  flex-direction: row;
  align-content: center;
  justify-content: center;
}

.position {
  width: 50px;
  height: 50px;
  border: 1px solid #000;
  margin: 5px;
  background-color: #ccc;

  &:hover {
    background-color: #3e8f3e;
  }

  &.player {
    background-color: #000;
  }
  &.enemy {
    background-color: red;
  }
}

.cards {
  height: 2px;
  border-top: 1px solid #ccc;
  margin-top: 15px;
  padding-top: 15px;
}

.cards_inner {
  display: flex;
  flex-direction: row;
  align-content: center;
  justify-content: center;
}

.card {
  padding: 20px;
  margin: 0 3px;
  background-color: #ccc;
  text-align: center;
}
</style>