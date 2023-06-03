/* eslint-disable */
<template>
  <div class="row ">
    <div class="col">
      <div class="row shadow-2">
        <div class="col-2 q-pa-md">
          <q-input v-model.number="summ" type="number" filled hint="Сумма" dense />
        </div>

        <div class="col-2 q-pa-md">
          <q-input v-model.number="months" type="number" filled hint="Срок в месяцах" dense />
        </div>
        <div class="col-2 q-pa-md">
          <q-input
           v-model.number="percent"
           type="number"
           step="0.1"
           filled
           hint="Процентная ставка"
           dense />
        </div>
        <div class="col-2 q-pa-md">
          <q-input filled v-model="date" mask="date" :rules="['date']" hint="Дата начала" dense>
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <q-date v-model="date">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Close" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
        <div class="col-2 q-pa-md">
          <q-btn class=" btn btn-info" color="secondary" @click="runCount">Расcчитать</q-btn>
        </div>
      </div>
      <div class="row shadow-2">
        <div class="col-2 q-pa-md">
          <q-input
          bg-color="green-2"
          ronded
          outlined
          v-model="monthPay"
          hint="Ежемесячный платеж"
          dense
          readonly />
        </div>
        <div class="col-2 q-pa-md">
          <q-input
          bg-color="green-2"
          ronded
          outlined
          v-model="overpay"
          hint="Переплата"
          dense
          readonly />
        </div>
        <div class="col-2 q-pa-md">
          <q-input
          bg-color="green-2"
          ronded
          outlined
          v-model="to_return"
          hint="Итоговая сумма к возврату"
          dense
          readonly />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { defineComponent, ref } from 'vue';
import axios from 'axios';

export default defineComponent({
  name: 'IndexPage',

  setup() {
    const summ = ref(0);
    const months = ref(0);
    const percent = ref(0);
    const monthPay = ref(0);
    const overpay = ref(0);
    const to_return = ref(0);
    return {
      summ,
      months,
      percent,
      monthPay,
      overpay,
      to_return,
      date: ref(''),
      runCount: function () {
        axios.post('http://127.0.0.1:5000/count_credit?summa=' + summ.value +
          '&percent=' + percent.value +
          '&months=' + months.value)
          .then(function (resp) {
            console.log(resp)
            monthPay.value = resp.data.month_sum
            overpay.value = resp.data.overpay
            to_return.value = overpay.value + summ.value
          }

          )
      }
    };
  },
});
</script>
