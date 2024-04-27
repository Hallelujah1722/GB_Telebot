<script setup>
import {
    dashboardOne,
    dashboardTwo,
    splineAreaWidgetTwo,
    splineAreaWidgetThree,
} from '@/data/dashboard.v1.js'

</script>

<template>
  <div class="container mx-auto">

    <div class="grid grid-cols-12 gap-5">
            <div
                class="
                    col-span-12
                    xl:col-span-4
                    lg:col-span-6
                    md:col-span-6
                    sm:col-span-6
                "
            >
                <BaseCard>
                    <div class="flex align-center">
                        <i class="i-Add-User text-6xl text-purple-200"></i>
                        <div class="m-auto">
                            <p class="text-gray-400">Отзывы о спикерах</p>
                            <p class="text-xl text-primary">205</p>
                        </div>
                    </div>
                </BaseCard>
            </div>
            <div
                class="
                    col-span-12
                    xl:col-span-4
                    lg:col-span-6
                    md:col-span-6
                    sm:col-span-6
                "
            >
                <BaseCard>
                    <div class="flex align-center">
                        <i class="i-Financial text-6xl text-purple-200"></i>
                        <div class="m-auto">
                            <p class="text-gray-400">Положительные</p>
                            <p class="text-xl text-primary">21</p>
                        </div>
                    </div>
                </BaseCard>
            </div>
            <div
                class="
                    col-span-12
                    xl:col-span-4
                    lg:col-span-6
                    md:col-span-6
                    sm:col-span-6
                "
            >
                <BaseCard>
                    <div class="flex align-center">
                        <i
                            class="i-Checkout-Basket text-6xl text-purple-200"
                        ></i>
                        <div class="m-auto">
                            <p class="text-gray-400">Релевантные</p>
                            <p class="text-xl text-primary">80</p>
                        </div>
                    </div>
                </BaseCard>
            </div>
      <div class="col-span-12 xl:col-span-6 md:col-span-6">
        <BaseCard>
          <h4 class="card-title mb-6">Релевантные/нерелевантные отзывы</h4>
          <apexchart
              type="pie"
              height="330"
              :options="dashboardTwo.chartOptions"
              :series="dashboardTwo.series"
          ></apexchart>
        </BaseCard>
      </div>

      <div class="col-span-12 xl:col-span-6 md:col-span-6">
        <BaseCard>
          <h4 class="card-title mb-6">Положительные/отрицательные отзывы</h4>
          <apexchart
              type="pie"
              height="330"
              :options="dashboardTwo.chartOptions"
              :series="dashboardTwo.series"
          ></apexchart>
        </BaseCard>
      </div>
    </div>
  </div>
</template>
