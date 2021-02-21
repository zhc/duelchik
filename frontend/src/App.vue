<template>
  <div class="arena">
    <div class="players">
      <div v-for="(n, ind) in size">
        <button class="position"
                :disabled="!canGoTo(ind)"
                :class="{ 'player' : isYourPos(ind), 'enemy' : isEnemyPos(ind) }"
                @click="moveTo(ind)"
                @mouseover="mouseOverPos(ind)" @mouseout="mouseOutPos"></button>
      </div>
    </div>
    <div class="cards">
      <div class="cards_inner">
        <div class="card" v-for="item in deck" :class="{ 'hover' : isMouseOver(item) }">
          <div class="card_number">{{ item }}</div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import store from "../src/store";

export default {
  data() {
    return {
      mouseOverInd: -1
    }
  },
  computed: {
    deck: function () {
      return store.getters.deck;
    },
    size: function () {
      return store.getters.size;
    },
  },
  created() {
  },
  methods: {
    moveTo: function (ind) {
      store.dispatch('getMessage', ind);
    },
    isYourPos: function (ind) {
      return ind === store.getters.playerIndex;
    },
    isEnemyPos: function (ind) {
      return ind === store.getters.enemyIndex;
    },
    canGoTo: function (ind) {
      return store.getters.deck.some(point => {
        if (ind === (store.getters.playerIndex + point)) {
          return true;
        }
        if (ind === (store.getters.playerIndex - point)) {
          return true;
        }
      });
    },
    mouseOverPos: function (ind) {
      this.mouseOverInd = ind;
    },
    mouseOutPos: function () {
      this.mouseOverInd = -1;
    },
    isMouseOver: function (point) {
      return this.mouseOverInd > -1 && (point === (this.mouseOverInd - store.getters.playerIndex) || point === (store.getters.playerIndex - this.mouseOverInd));
    }
  }
}
</script>
<style lang="scss">
html {
  font-family: Georgia, Arial, sans-serif;
  font-size: 100%;
  line-height: 1;
  color: #464546;
}

body {
  height: 100%;
}

.arena {
  display: flex;
  flex-direction: column;
  align-content: center;
  height: 100%;
}

.players {
  display: flex;
  flex-direction: row;
  align-content: center;
  justify-content: center;
}

.position {
  width: 42px;
  height: 42px;
  margin: 0 5px;
  border-radius: 3px;
  background-color: lightgreen;
  border: 1px solid green;
  transition: background-color .2s linear, border-color .2s linear;

  &:focus {
    outline: none;
  }

  &:hover {
    cursor: pointer;
  }

  &:disabled {
    cursor: default;
    background-color: #f1f1f1;
    border: 1px solid #e1e1e1;
  }

  &.player {
    background-color: #000;
    border-color: #000;
  }

  &.enemy {
    background-color: red;
    border-color: darkred;
  }
}

.cards {
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
  width: 110px;
  height: 150px;
  margin: 0 10px;
  box-shadow: 2px 5px 10px #f1f1f1;
  background-color: #fff;
  border-radius: 5px;
  border: 1px solid #e1e1e1;
  position: relative;
  transition: margin-top .2s linear;

  &_number {
    position: absolute;
    text-align: center;
    top: calc(50% - 21px);
    left: calc(50% - 15px);
    width: 30px;
    font-size: 42px;
    line-height: 1;
  }

  &.hover {
    margin-top: 10px;
  }
}
</style>