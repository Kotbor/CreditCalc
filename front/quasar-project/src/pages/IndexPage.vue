/* eslint-disable */
<template>
  <div class="row ">
    <div class="col">
      <div class="row shadow-2">
        <div class="col-auto q-pa-md">
          <q-input v-model.number="summ" type="number" filled hint="Сумма" dense />
        </div>

        <div class="col-auto q-pa-md">
          <q-input v-model.number="months" type="number" filled hint="Срок в месяцах" dense />
        </div>
        <div class="col-auto q-pa-md">
          <q-input
           v-model.number="percent"
           type="number"
           step="0.1"
           filled
           hint="Процентная ставка"
           dense />
        </div>

        <div class="col-2 q-pa-md">
          <q-btn class=" btn btn-info" color="secondary" @click="runCount">Расcчитать</q-btn>
        </div>
      </div>
      <div class="row shadow-2">
        <div class="col-auto q-pa-md">
          <q-input
          bg-color="green-2"
          ronded
          outlined
          v-model="monthPay"
          hint="Ежемесячный платеж"
          dense
          readonly />
        </div>
        <div class="col-auto q-pa-md">
          <q-input
          bg-color="green-2"
          ronded
          outlined
          v-model="overpay"
          hint="Переплата"
          dense
          readonly />
        </div>
        <div class="col-auto q-pa-md">
          <q-input
          bg-color="green-2"
          ronded
          outlined
          v-model="to_return"
          hint="Итоговая сумма к возврату"
          dense
          readonly />
        </div>
        <div class="col-2 q-pa-md">
          <q-btn class=" btn btn-info" color="deep-orange"
          @click="creditToInvest"> Кредит В инвестиции</q-btn>
        </div>
      </div>

      <div class="row shadow-2">
        <div class="col-auto q-pa-md">
          <q-input
          ref = "dateeRef"
          filled
          v-model="date"
          hint="Дата начала"
          lazy-rules
          :rules="daterules"
          dense>
            <template v-slot:append>
              <q-icon name="event" class="cursor-pointer">
                <q-popup-proxy cover transition-show="scale" transition-hide="scale">
                  <q-date v-model="date" mask="DD.MM.YYYY">
                    <div class="row items-center justify-end">
                      <q-btn v-close-popup label="Закрыть" color="primary" flat />
                    </div>
                  </q-date>
                </q-popup-proxy>
              </q-icon>
            </template>
          </q-input>
        </div>
        <div class="col-auto q-pa-md">
          <q-input
           v-model.number="total_investments"
          type="number"
          filled
          hint="Всего инвестиций" dense />
        </div>
        <div class="col-auto q-pa-md">
          <q-input
           v-model.number="our_investments_percent"
          type="number"
          filled
          hint="Процент наших инвестиций"
          :max-decimals="2"
          dense
          @update:model-value="newvalue => sumFromPercents(newvalue)"/>

        </div>
        <div class="col-auto q-pa-md">
          <q-input
           v-model.number="our_investments_sum"
          type="number"
          filled
          hint="Сумма наших инвестиций"
          dense
          @update:model-value="newvalue => percentsFromSum(newvalue)"/>
        </div>
        <div class="col-auto q-pa-md">
          <q-input
           v-model.number="object_profit"
          type="number"
          filled
          hint="Выручка объекта" dense />
        </div>
        <div class="col-auto q-pa-md">
          <q-input
           v-model.number="profit_return_percent_while_not_inv_returned"
          type="number"
          filled
          hint="Процент с выручки до возврата" dense />
        </div>
        <div class="col-auto q-pa-md">
          <q-input
           v-model.number="profit_return_percent_after_inv_returned"
          type="number"
          filled
          hint="Процент с выручки после возврата" dense />
        </div>
        <div class="col-2 q-pa-md">
          <q-btn class="btn btn-info"  @click="runWhenToPlus" color="green" >Рассчитать</q-btn>
        </div>

      </div>

    </div>
    </div>
    <div class="row">
      <div class="col">
        <div>
        <apexchart height="500" type="area" :options="options" :series="series"></apexchart>
        </div>
      </div>
    </div>

    <div class="row">
      <div class="col">
      <q-markup-table dense>
      <thead class="bg-light-blue-3">
        <tr >
          <th class="text-center">Дата</th>
          <th class="text-center">Выручка</th>
          <th class="text-center">К возврату</th>
          <th class="text-center">Всего вернули</th>
          <th class="text-center">Наш баланс</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="row in payment_list" :key="row.number"
        :class="(row.our_balance>0)?'bg-green-1':'bg-red-1'">

          <td class="text-center">{{ row.date }}</td>
          <td class="text-center">{{ row.profit }}</td>
          <td class="text-center">{{ row.sum_return_this_month }}</td>
          <td class="text-center">{{ row.returned_sum }}</td>
          <td class="text-center">{{ row.our_balance }}</td>
        </tr>
      </tbody>
      </q-markup-table>
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
    const date = ref('')
    const dateRef = ref('')
    const total_investments=ref(0);
    const our_investments_percent=ref(0);
    const our_investments_sum=ref(0);
    const object_profit=ref(0);
    const profit_return_percent_while_not_inv_returned=ref(0);
    const profit_return_percent_after_inv_returned=ref(0);
    const payment_list = ref([]);
    const options = ref({
        chart: {
          id: 'payments-graph'
        },
        xaxis: {
          categories: []
        }
      });
      const series = ref([{
        name: 'Наш баланс',
        data: []
      }]);

    return {
      summ,
      months,
      percent,
      monthPay,
      overpay,
      to_return,
      total_investments,
      our_investments_percent,
      our_investments_sum,
      object_profit,
      profit_return_percent_after_inv_returned,
      profit_return_percent_while_not_inv_returned,
      date,
      payment_list,
      options,
      series,
      dateRef,
      daterules:[ val => val.length>= 8 || 'Введите данные'],
      runCount: function () {
        axios.post('/count_credit?summa=' + summ.value +
          '&percent=' + percent.value +
          '&months=' + months.value)
          .then(function (resp) {
            console.log(resp)
            monthPay.value = resp.data.month_sum
            overpay.value = resp.data.overpay
            to_return.value = overpay.value + summ.value

          }

          )
      },
      runWhenToPlus: function () {


        axios.post('/when_to_plus?begin=' + date.value +
        '&total_investments=' + total_investments.value +
        '&our_investments_percent=' + our_investments_percent.value+
        '&object_profit=' + object_profit.value+
        '&profit_return_percent_while_not_inv_returned=' + profit_return_percent_while_not_inv_returned.value+
        '&profit_return_percent_after_inv_returned=' + profit_return_percent_after_inv_returned.value
        )
          .then(function (resp) {
            console.log(resp)
            payment_list.value=resp.data
            let balance = payment_list.value.map(v => v.our_balance)
            let dates = payment_list.value.map(v => v.date)
            series.value = [{
              name: 'Наш баланс',
              data: balance
            }]
            options.value = {
            chart: {
              id: 'payments-graph'
            },
            xaxis: {
              categories: dates
            }
          }

          }

          )
      },
      sumFromPercents: function (perc) {
        if (perc){
          our_investments_sum.value = total_investments.value*perc/100
        }
      },
      percentsFromSum: function (summ) {
        if (summ)
        {
          our_investments_percent.value =(summ*100/total_investments.value).toFixed(2)
        }
      },
      creditToInvest: function(){
        our_investments_sum.value=to_return.value
        if (total_investments.value){
          our_investments_percent.value = (to_return.value*100/total_investments.value).toFixed(2)
        }
        else {
          total_investments.value = to_return.value
          our_investments_percent.value = (to_return.value*100/total_investments.value).toFixed(2)
        }
      },
      // updateTotalInvestSum: function(){
      //   if (our_investments_sum.value && total_investments.value){
      //     our_investments_percent.value = our_investments_sum.value*100/total_investments.value
      //   }
      //   else if (our_investments_percent.value){
      //     our_investments_sum.value = total_investments.value*our_investments_percent.value/100
      //   }

      // }
    };
  },
});
</script>
