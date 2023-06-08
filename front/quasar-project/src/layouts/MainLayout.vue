<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>

        <q-toolbar-title>
          Расчёт платежей
        </q-toolbar-title>

        <div></div>
      </q-toolbar>
    </q-header>

    <q-page-container style="background-color: #F6F6F6;">
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'MainLayout',

  setup() {
    return {
    };
  },
});
</script>
