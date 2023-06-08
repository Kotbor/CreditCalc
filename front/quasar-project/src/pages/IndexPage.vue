/* eslint-disable */
<template>
  <div
    class="full-height full-width row justify-center items-center row q-pa-md shadow-4"
  >
    <div class="col-auto">
      <div class="col-auto">
        <q-card class="my-card" style="">
          <q-card-section>
            <div class="text-subtitle2">Параметры инвестиций</div>
          </q-card-section>
          <q-card-section class="q-pt-none">
            <div class="row">
              <div class="col-auto">
                <div class="col-auto q-pa-md">
                  <q-input
                    ref="dateRef"
                    outlined
                    v-model="date"
                    hint="Дата начала"
                    lazy-rules
                    :rules="daterules"
                    dense
                  >
                    <template v-slot:append>
                      <q-icon name="event" class="cursor-pointer">
                        <q-popup-proxy
                          cover
                          transition-show="scale"
                          transition-hide="scale"
                        >
                          <q-date v-model="date" mask="DD.MM.YYYY">
                            <div class="row items-center justify-end">
                              <q-btn
                                v-close-popup
                                label="Закрыть"
                                color="primary"
                                flat
                              />
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
                    outlined
                    hint="Всего инвестиций в объект"
                    dense
                  />
                </div>
                <div class="col-auto q-pa-md">
                  <q-input
                    v-model.number="our_investments_percent"
                    type="number"
                    outlined
                    hint="Процент наших инвестиций"
                    :max-decimals="2"
                    dense
                    @update:model-value="
                      (newvalue) => sumFromPercents(newvalue)
                    "
                  />
                </div>
                <div class="col-auto q-pa-md">
                  <q-input
                    v-model.number="our_investments_sum"
                    type="number"
                    outlined
                    hint="Сумма наших инвестиций"
                    dense
                    @update:model-value="
                      (newvalue) => percentsFromSum(newvalue)
                    "
                  />
                </div>
              </div>
              <div class="col-auto">
                <div class="col-auto q-pa-md">
                  <q-input
                    v-model.number="object_profit"
                    type="number"
                    outlined
                    hint="Выручка объекта"
                    dense
                  />
                </div>
                <div class="col-auto q-pa-md">
                  <q-input
                    v-model.number="
                      profit_return_percent_while_not_inv_returned
                    "
                    type="number"
                    outlined
                    hint="Процент с выручки до возврата"
                    dense
                  />
                </div>
                <div class="col-auto q-pa-md">
                  <q-input
                    v-model.number="profit_return_percent_after_inv_returned"
                    type="number"
                    outlined
                    hint="Процент с выручки после возврата"
                    dense
                  />
                </div>
                <div class="col-auto q-pa-md">
                  <q-toggle v-model="toCredit" label="Инвестиции в кредит" />
                </div>
              </div>
              <div class="col-auto">
                <div class="col-auto q-pa-md">
                  <q-input
                    v-model.number="no_profit_months"
                    type="number"
                    outlined
                    hint="Месяцев без прибыли"
                    dense
                  />
                </div>
                <div class="col-auto q-pa-md">
                  <q-input
                    v-model.number="months_after_refund"
                    type="number"
                    outlined
                    hint="Сколько месяцев показывать после окупаемости"
                    dense
                  />
                </div>
                <div class="col-auto q-pa-md">
                  <q-input
                    v-model.number="our_investments_count_sum"
                    type="number"
                    outlined
                    hint="Сумма для расчёта"
                    dense
                    disable
                    readonly
                  />
                </div>

                <div class="col-auto q-pa-md">
                  <q-btn
                    class="btn btn-info full-width"
                    @click="runWhenToPlus"
                    color="green"
                    no-caps
                    >Построить график</q-btn
                  >
                </div>
              </div>
            </div>
          </q-card-section>
        </q-card>
      </div>
    </div>
    <div class="col-auto q-pa-md">
      <div class="full-height full-width row justify-center items-center">
        <div class="col self-center">
          <q-card class="my-card" style="">
            <q-card-section>
              <div class="text-subtitle2">Параметры кредита</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
              <div class="col-auto q-pa-md">
                <q-input
                  v-model.number="credit_summ"
                  type="number"
                  outlined
                  hint="Сумма кредита"
                  dense
                />
              </div>
              <div class="col-auto q-pa-md">
                <q-input
                  v-model.number="months"
                  type="number"
                  outlined
                  hint="Срок кредита в месяцах"
                  dense
                />
              </div>
              <div class="col-auto q-pa-md">
                <q-input
                  v-model.number="percent"
                  type="number"
                  step="0.1"
                  outlined
                  hint="Процентная ставка"
                  dense
                />
              </div>
            </q-card-section>
          </q-card>
        </div>
        <div class="col self-center q-pa-md">
          <q-card class="my-card" style="">
            <q-card-section>
              <div class="text-subtitle2">Результат расчетов кредита</div>
            </q-card-section>

            <q-card-section class="q-pt-none">
              <div class="col-auto q-pa-md">
                <q-input
                  bg-color="green-2"
                  ronded
                  outlined
                  v-model="monthPay"
                  hint="Ежемесячный платеж"
                  dense
                  readonly
                />
              </div>
              <div class="col-auto q-pa-md">
                <q-input
                  bg-color="green-2"
                  ronded
                  outlined
                  v-model="overpay"
                  hint="Переплата"
                  dense
                  readonly
                />
              </div>
              <div class="col-auto q-pa-md">
                <q-input
                  bg-color="green-2"
                  ronded
                  outlined
                  v-model="to_return"
                  hint="Итоговая сумма к возврату"
                  dense
                  readonly
                />
              </div>
            </q-card-section>
          </q-card>
        </div>
        <div class="col-auto self-center q-pa-md">
          <q-card class="my-card" >
            <q-card-section>
              <div class="text-subtitle2">Процент переплаты</div>
            </q-card-section>

            <q-card-section class="q-pt-none" >
                <div>
                  <apexchart
                    type="pie"
                    width="350"
                    :options="pieoptions"
                    :series="pieseries"
                  ></apexchart>
              </div>
            </q-card-section>
          </q-card>
        </div>
      </div>
    </div>
  </div>
  <div class="row q-pa-md">
    <div class="col">
      <div>
        <apexchart
          height="500"
          type="area"
          :options="options"
          :series="series"
        ></apexchart>
      </div>
    </div>
  </div>

  <div class="row q-pa-md">
    <div class="col">
      <q-markup-table dense>
        <thead class="bg-blue-6">
          <tr>
            <th class="text-center text-white">Дата</th>
            <th class="text-center text-white">Выручка</th>
            <th class="text-center text-white">К возврату</th>
            <th class="text-center text-white">Всего вернули</th>
            <th class="text-center text-white">Наш баланс</th>
          </tr>
        </thead>
        <tbody>
          <tr
            v-for="row in payment_list"
            :key="row.number"
            :class="row.our_balance > 0 ? 'bg-green-1' : 'bg-red-1'"
          >
            <td class="text-center">{{ row.date }}</td>
            <td class="text-center">{{ row.profit }}</td>
            <td class="text-center">{{ row.sum_return_this_month }}</td>
            <td class="text-center">{{ row.returned_sum }}</td>
            <td class="text-center">{{ row.our_balance }}</td>
          </tr>
        </tbody>
      </q-markup-table>
    </div>
    <div>
      <q-dialog v-model="alert">
        <q-card>
          <q-card-section>
            <div class="text-h6">Внимание</div>
          </q-card-section>

          <q-card-section class="q-pt-none">
            Необходимо заполнить срок кредита и процентную ставку
          </q-card-section>

          <q-card-actions align="right">
            <q-btn flat label="OK" color="primary" v-close-popup />
          </q-card-actions>
        </q-card>
      </q-dialog>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
import { defineComponent, ref } from "vue";
import axios from "axios";
import { watch } from "vue";

export default defineComponent({
  name: "IndexPage",

  setup() {
    var count = ref(1);
    const alert = ref(false);
    const credit_summ = ref();
    const months = ref(60);
    const no_profit_months = ref(3);
    const percent = ref(12);
    const toCredit = ref(false);
    const monthPay = ref();
    const overpay = ref();
    const to_return = ref();
    const date = ref(new Date().toLocaleDateString());
    const dateRef = ref("");
    const total_investments = ref();
    const our_investments_percent = ref();
    const our_investments_sum = ref();
    const our_investments_count_sum = ref();
    const object_profit = ref();
    const profit_return_percent_while_not_inv_returned = ref();
    const profit_return_percent_after_inv_returned = ref();
    const payment_list = ref([]);
    const months_after_refund = ref(12);
    const options = ref({
      chart: {
        id: "payments-graph",
      },
      xaxis: {
        categories: [],
      },
    });
    const series = ref([]);
    const pieoptions = {
        labels: ['Сумма кредита', 'Переплата'],
        colors:['#1E61F2', '#E91E63'],
        legend:{position:'bottom'}
    }
    const pieseries =  ref([0, 0]);
    const runCount = function () {
      axios
        .post(
          "http://localhost:34567/api/count_credit?summa=" +
            credit_summ.value +
            "&percent=" +
            percent.value +
            "&months=" +
            months.value
        )
        .then(function (resp) {
          console.log(resp);
          monthPay.value = resp.data.month_sum;
          overpay.value = resp.data.overpay;
          to_return.value = overpay.value + credit_summ.value;
          if (toCredit.value) {
            our_investments_count_sum.value = to_return.value;
          }
          pieseries.value=[credit_summ.value,overpay.value]
        });
    };

    const count_credit_sum = function () {
      if (months.value && percent.value) {
        credit_summ.value = our_investments_sum.value;
        runCount();
      } else {
        alert.value = true;
        toCredit.value = false;
      }
    };
    watch(toCredit, (value) => {
      if (value == true) {
        count_credit_sum();
      } else {
        our_investments_count_sum.value = our_investments_sum.value;
      }
    });
    watch(our_investments_sum, (value) => {
      if (toCredit.value == true) {
        count_credit_sum();
      } else {
        our_investments_count_sum.value = our_investments_sum.value;
      }
    });
    watch(percent, (value) => {
      if (value){
      count_credit_sum();
      }
    });
    watch(months, (value) => {
      if (value){
      count_credit_sum();
      }
    });

    return {
      count,
      alert,
      credit_summ,
      months,
      no_profit_months,
      percent,
      toCredit,
      monthPay,
      overpay,
      to_return,
      total_investments,
      our_investments_percent,
      our_investments_sum,
      our_investments_count_sum,
      object_profit,
      profit_return_percent_after_inv_returned,
      profit_return_percent_while_not_inv_returned,
      date,
      payment_list,
      options,
      series,
      pieoptions,
      pieseries,
      dateRef,
      runCount,
      months_after_refund,
      daterules: [(val) => val.length >= 8 || "Введите данные"],

      runWhenToPlus: function () {
        axios
          .post(
            "http://localhost:34567/api/when_to_plus?begin=" +
              date.value +
              "&total_investments=" +
              total_investments.value +
              "&our_investments=" +
              our_investments_count_sum.value +
              "&object_profit=" +
              object_profit.value +
              "&profit_return_percent_while_not_inv_returned=" +
              profit_return_percent_while_not_inv_returned.value +
              "&profit_return_percent_after_inv_returned=" +
              profit_return_percent_after_inv_returned.value +
              "&months_after_refund=" +
              months_after_refund.value +
              "&no_profit_months=" +
              no_profit_months.value
          )
          .then(function (resp) {
            console.log(resp);
            payment_list.value = resp.data;
            let balance = payment_list.value.map((v) => v.our_balance);
            let dates = payment_list.value.map((v) => v.date);

            series.value.push({
              name: "Баланс № " + count.value,
              data: balance,
            });
            count.value++;
            options.value = {
              chart: {
                id: "payments-graph",
              },
              xaxis: {
                categories: dates,
              },
            };
          });
      },
      sumFromPercents: function (perc) {
        if (perc) {
          our_investments_sum.value = (total_investments.value * perc) / 100;
        }
      },
      percentsFromSum: function (summ) {
        if (summ) {
          our_investments_percent.value = (
            (summ * 100) /
            total_investments.value
          ).toFixed(2);
        }
      },
      creditToInvest: function () {
        our_investments_sum.value = to_return.value;
        if (total_investments.value) {
          our_investments_percent.value = (
            (to_return.value * 100) /
            total_investments.value
          ).toFixed(2);
        } else {
          total_investments.value = to_return.value;
          our_investments_percent.value = (
            (to_return.value * 100) /
            total_investments.value
          ).toFixed(2);
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
