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
                            <p class="text-gray-400">Отзывы о контенте</p>
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




      <div class="col-span-12">
        <BaseCard>
          <template v-slot:cardHeader>
            <div class="card-header">
              <div class="card-title py-3 text-center">Рейтинг контента</div>
            </div>
          </template>
          <div
              class="
                            block
                            w-full
                            overflow-x-auto
                            whitespace-nowrap
                            borderless
                            hover
                        "
          >
            <div
                class="
                                dataTable-wrapper dataTable-loading
                                no-footer
                                fixed-columns
                            "
            >
              <div
                  class="
                                    dataTable-container
                                    block
                                    w-full
                                    overflow-x-auto
                                    whitespace-nowrap
                                    borderless
                                    hover
                                "
              >
                <table
                    class="
                                        table-3
                                        dataTable-table
                                        max-w-full
                                        w-full
                                    "
                >
                  <thead>
                  <tr class="">
                    <th
                        class="
                                                    text-left
                                                    border-b
                                                    pb-3
                                                    mb-3
                                                    text-gray-500
                                                    font-semibold
                                                "
                    >
                      №
                    </th>
                    <th
                        class="
                                                    text-left
                                                    border-b
                                                    pb-3
                                                    mb-3
                                                    text-gray-500
                                                    font-semibold
                                                "
                    >
                      Название
                    </th>
                    <th
                        class="
                                                    text-left
                                                    border-b
                                                    pb-3
                                                    mb-3
                                                    text-gray-500
                                                    font-semibold
                                                "
                    >
                      Отзывы
                    </th>
                    <th
                        class="
                                                    text-left
                                                    border-b
                                                    pb-3
                                                    mb-3
                                                    text-gray-500
                                                    font-semibold
                                                "
                    >
                      Релевантные
                    </th>
                    <th
                        class="
                                                    text-left
                                                    border-b
                                                    pb-3
                                                    mb-3
                                                    text-gray-500
                                                    font-semibold
                                                "
                    >
                      Нерелевантные
                    </th>
                    <th
                        class="
                                                    text-left
                                                    border-b
                                                    pb-3
                                                    mb-3
                                                    text-gray-500
                                                    font-semibold
                                                "
                    >
                      Положительные
                    </th>
                     <th
                        class="
                                                    text-left
                                                    border-b
                                                    pb-3
                                                    mb-3
                                                    text-gray-500
                                                    font-semibold
                                                "
                    >
                      Отрицательные
                    </th>
                    <th
                        class="
                                                    text-left
                                                    border-b
                                                    pb-3
                                                    mb-3
                                                    text-gray-500
                                                    font-semibold
                                                "
                    >

                    </th>
                  </tr>
                  </thead>
                  <tbody>
                  <tr
                      class="
                                                hover:bg-gray-100
                                                cursor-pointer
                                            "
                      v-for="(n, index) in 8"
                      :key="index"
                  >
                    <td class="text-xs py-5 px-4">
                      {{ index + 1 }}
                    </td>

                    <td class="text-xs">
                      ааапппп {{ index + 1 }}
                    </td>

                    <td class="py-5">
                                                <span
                                                    class="
                                                        px-3
                                                        py-1
                                                        rounded-full
                                                        text-primary
                                                        border border-primary
                                                        mr-3
                                                        text-xs
                                                    "
                                                >Delivered</span
                                                >
                    </td>
                    <td class="py-5">
                      {{ 3.34 * index + 1 }}%
                    </td>
                    <td class="py-5">
                      {{ 3.34 * index + 1 }}%
                    </td>
                    <td class="py-5">
                      {{ 3.34 * index + 1 }}%
                    </td>
                    <td class="py-5">12-02-20</td>
                    <td class="py-5">
                      <BaseBtn
                          rounded
                          class="
                                                        border border-primary
                                                        text-primary
                                                        hover:bg-primary
                                                        hover:text-white
                                                    "
                      >
                        Смотреть подробнее
                      </BaseBtn>
                    </td>
                  </tr>
                  </tbody>
                </table>
              </div>
            </div>
          </div>
        </BaseCard>
      </div>













      <div class="col-span-12 xl:col-span-12 md:col-span-12 text-center mt-5">
          <h1 class="mt-6">Основы программирования</h1>
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


      <div class="col-span-12 xl:col-span-12 md:col-span-12 text-center mt-5">
          <h1 class="mt-6">Продвинутые техники программирования</h1>
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


      <div class="col-span-12 xl:col-span-12 md:col-span-12 text-center mt-5">
          <h1 class="mt-6">ChatGPT для обучения</h1>
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


      <div class="col-span-12 xl:col-span-12 md:col-span-12 text-center mt-5">
          <h1 class="mt-6">Java api браузеров</h1>
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

      <div class="col-span-12 xl:col-span-12 md:col-span-12 text-center mt-5">
          <h1 class="mt-6">Знакомство с языком Python</h1>
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


      <div class="col-span-12 xl:col-span-12 md:col-span-12 text-center mt-5">
          <h1 class="mt-6">Новейшие тенденции в IT</h1>
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

      <div class="col-span-12 xl:col-span-12 md:col-span-12 text-center mt-5">
          <h1 class="mt-6">Управление персоналом</h1>
      </div>

      <div class="col-span-12 xl:col-span-6 md:col-span-6 mb-10">
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

      <div class="col-span-12 xl:col-span-6 md:col-span-6 mb-10">
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
