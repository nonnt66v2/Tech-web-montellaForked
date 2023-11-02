let cacheName = 'pwa01'
let filesToCache = [
    'index.html',
    'css/css.css',
    'js/main.js'
]
/**
 * inizializza il service worker e la cache di tutti contenuti delle app
 */
self.addEventListener('install',function (e){
    e.waitUntil(
        caches.open(cacheName).then(function (cache){
            return cache.addAll(filesToCache);
        })
    )
})
/**
 * mostra i contenuti salvati nella cache quando si è offline
 */
self.addEventListener('fetch',function(e){
    e.respondWith(
        caches.match(e.request).then(function(response){
            return response || fetch(e.request);
        })
    )
})