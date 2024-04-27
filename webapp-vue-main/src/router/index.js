import { createRouter, createWebHistory } from 'vue-router'
import NotFound from '../views/NotFound.vue'
import store from '../store'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('../layout/index.vue'),
        redirect: '/dashboards/dashboard-version-one',
        meta: {
            title: 'Home',
        },

        children: [
            {
                path: '/dashboards',
                name: 'Dashboards',
                component: () => import('../views/dashboards/index.vue'),
                meta: {
                    title: 'Dashboard',
                },
                children: [
                    {
                        path: 'dashboard-version-one',
                        name: 'dashboard-version-one',
                        component: () =>
                            import('../views/dashboards/Dashboards.v1.vue'),
                    },
                ],
            },
            {
                path: '/components',
                name: 'components',
                component: () => import('../views/components/index.vue'),
                meta: {
                    title: 'Components',
                },
                children: [
                    {
                        path: 'button',
                        name: 'button',
                        component: () =>
                            import('../views/components/Button.vue'),
                    },
                ],
            },
            {
                path: '/signIn',
                name: 'signIn',
                component: () => import('../views/profile/SignIn.vue'),
                meta: {
                    title: 'signIn',
                },

            },
            {
                path: '/signUp',
                name: 'signUp',
                component: () => import('../views/sessions/SignUp.vue'),
                meta: {
                    title: 'signUp',
                },

            },
        ],
    },



    { path: '/:path(.*)', component: NotFound },
]

const router = createRouter({
    history: createWebHistory(),
    scrollBehavior(to, from, savedPosition) {
        return { left: 0, top: 0 }
    },
    routes,
})

router.afterEach(() => {
    if (window.innerWidth <= 1200) {
        const sidenav =
            store.state.largeSidebar.sidebarToggleProperties.isSideNavOpen

        store.commit('largeSidebar/toggleSidebarProperties')
    }
})

export default router
