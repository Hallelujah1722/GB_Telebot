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
                    xl:col-span-3
                    lg:col-span-6
                    md:col-span-6
                    sm:col-span-6
                "
            >
                <BaseCard>
                    <div class="flex align-center">
                        <i class="i-Add-User text-6xl text-purple-200"></i>
                        <div class="m-auto">
                            <p class="text-gray-400">Количество отзывов</p>
                            <p class="text-xl text-primary">205</p>
                        </div>
                    </div>
                </BaseCard>
            </div>
            <div
                class="
                    col-span-12
                    xl:col-span-3
                    lg:col-span-6
                    md:col-span-6
                    sm:col-span-6
                "
            >
                <BaseCard>
                    <div class="flex align-center">
                        <i class="i-Financial text-6xl text-purple-200"></i>
                        <div class="m-auto">
                            <p class="text-gray-400">Отзывы о спикерах</p>
                            <p class="text-xl text-primary">21</p>
                        </div>
                    </div>
                </BaseCard>
            </div>
            <div
                class="
                    col-span-12
                    xl:col-span-3
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
                            <p class="text-gray-400">Отзывы о контенте</p>
                            <p class="text-xl text-primary">80</p>
                        </div>
                    </div>
                </BaseCard>
            </div>
            <div
                class="
                    col-span-12
                    xl:col-span-3
                    lg:col-span-6
                    md:col-span-6
                    sm:col-span-6
                "
            >
                <BaseCard>
                    <div class="flex align-center">
                        <i class="i-Money-2 text-6xl text-purple-200"></i>
                        <div class="m-auto">
                            <p class="text-gray-400">Отзывы об организации</p>
                            <p class="text-xl text-primary">120</p>
                        </div>
                    </div>
                </BaseCard>
            </div>



            <div class="col-span-12 xl:col-span-12 md:col-span-6">
                <BaseCard>
                    <h4 class="card-title mb-4">Годовая статистика прохождения опроса</h4>
                    <apexchart
                        type="bar"
                        height="355"
                        :options="dashboardOne.chartOptions"
                        :series="dashboardOne.series"
                    ></apexchart>
                </BaseCard>
            </div>

        </div>
    </div>
</template>
