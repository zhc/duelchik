<template>
  <div class="arena">
    <div class="system_messages" v-if="systemMessage !== ''" v-html="systemMessage"></div>
    <div class="session" v-if="!gameStarted">
      <div class="session_inner">
        <input class="session_host" v-model="server" placeholder="http://127.0.0.1"/>
        <input class="session_id" v-model="session" placeholder="Enter session id"/>
        <button type="button" class="session_btn" :disabled="!hostDataIsValid" @click="startGameSession">Fight!</button>
      </div>
    </div>
    <div class="" v-if="gameStarted">
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
  </div>
</template>
<script>
import store from "../src/store";

export default {
  data() {
    return {
      mouseOverInd: -1,
      pingTimer: null,
      session: '',
      server: store.getters.host,
    }
  },
  computed: {
    hostDataIsValid() {
      return this.session !== '' && this.server !== '';
    },
    deck: function () {
      return store.getters.deck;
    },
    size: function () {
      return store.getters.size;
    },
    state() {
      return store.getters.state;
    },
    gameStarted() {
      return store.getters.token !== '';
    },
    systemMessage() {
      if (store.getters.state === 'WAITING_PLAYER') {
        return 'Waiting for the second player...';
      }
      if (store.getters.state === 'GAME_OVER') {
        if (store.getters.win) {
          return '<strong>YOU WIN!</strong>';
        } else {
          return '<strong>YOU LOSE!</strong>';
        }
      }
      if (store.getters.state === 'YOUR_TURN') {
        return 'YOUR TURN...';
      }
      if (store.getters.state === 'ENEMY_TURN') {
        return 'ENEMY TURN...';
      }
      if (store.getters.state === 'ERROR') {
        return 'ERROR!!! ' + store.getters.errorMessage;
      }
      return '';
    },
  },
  created() {

  },
  watch: {
    state(newState, oldState) {
      if (newState === 'GAME_OVER') {
        store.dispatch('pong');
      }
    }
  },
  methods: {
    startGameSession() {
      store.commit('setHost', this.server);
      store.dispatch('getToken', this.session).then(() => {
        store.dispatch('ping');
      });
    },
    moveTo: function (ind) {
      let moveCard = ind - store.getters.playerIndex;
      store.dispatch('getMessage', moveCard);
    },
    isYourPos: function (ind) {
      return ind === store.getters.playerIndex;
    },
    isEnemyPos: function (ind) {
      return ind === store.getters.enemyIndex;
    },
    canGoTo: function (ind) {
      if (store.getters.state === 'YOUR_TURN') {
        return store.getters.deck.some(point => {
          if (ind === (store.getters.playerIndex + point)) {
            return true;
          }
          if (ind === (store.getters.playerIndex - point)) {
            return true;
          }
        });
      } else {
        return false;
      }
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
  padding-top: 280px;
  background: #fff url('./assets/espada-eskrim.jpg') center -150px no-repeat;
}

.session {
  display: flex;
  justify-content: center;
  align-content: center;
  &_inner {
    width: 300px;
  }
  &_host,
  &_id {
    display: block;
    width: 100%;
    box-sizing: border-box;
    padding: 10px;
    &:focus {
      outline: none;
    }
  }
  &_host {
    margin-bottom: 10px;
  }
  &_btn {
    padding: 10px;
    display: block;
    width: 100%;
    box-sizing: border-box;
    margin-top: 10px;
    cursor: pointer;
  }
}

.system_messages {
  text-align: center;
  padding: 15px 0;
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
