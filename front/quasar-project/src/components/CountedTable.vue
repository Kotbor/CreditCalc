<template>
<q-markup-table>
  <thead>
    <tr>
    <th class="text-center">Номер</th>
    <th class="text-center">Всего инвестиций</th>
    <th class="text-center">Процент наших инвестиций</th>
    <th class="text-center">Сумма наших инвестиций</th>
    <th class="text-center">Прибыль объекта</th>
    <th class="text-center">Процент с прибыли до возврата</th>
    <th class="text-center">Процент с прибыли после возврата</th>
    <th class="text-center">Месяцев без прибыли</th>
    <th class="text-center">Возврат инвестиций, мес</th>
    <th class="text-center">Кредит</th>
    <th class="text-center">Сумма для расчёта</th>

  </tr>
  </thead>
  <tbody>
    <tr v-for="item in countedList" :key="item.count_num">
      <td class="text-center">{{item.count_num}}</td>
      <td class="text-center">{{ item.total_investments }}</td>
      <td class="text-center">{{ item.our_investments_percent }}</td>
      <td class="text-center">{{ item.our_investments_sum }}</td>
      <td class="text-center">{{ item.object_profit }}</td>
      <td class="text-center">{{ item.percent_not_returned }}</td>
      <td class="text-center">{{ item.percent_after_returned }}</td>
      <td class="text-center">{{ item.no_profit_months }}</td>
      <td class="text-center">{{ item.months_to_profit }}</td>
      <td class="text-center">{{ item.credit }}</td>
      <td class="text-center">{{ item.our_investments_count_sum }}</td>
    </tr>
  </tbody>

</q-markup-table>
</template>

<script>
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CountedTable',
  props: {
    countedList: {
      type: Array,
      required: true,
    },
  },

});
</script>
