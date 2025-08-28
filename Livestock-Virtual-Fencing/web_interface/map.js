const map = L.map('map').setView([0, 0], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { maxZoom: 19 }).addTo(map);
let marker;
const ws = new WebSocket('ws://' + window.location.host + '/ws');

ws.onmessage = function(event) {
  const data = JSON.parse(event.data);
  const lat = data.lat;
  const lng = data.lng;
  if (!marker) {
    marker = L.marker([lat, lng]).addTo(map);
    map.setView([lat, lng], 15);
  } else {
    marker.setLatLng([lat, lng]);
  }
  document.getElementById('coordinates').textContent = `Latitude: ${lat.toFixed(6)}, Longitude: ${lng.toFixed(6)}`;
};

document.getElementById('move-form').addEventListener('submit', function(event) {
  event.preventDefault();
  const lat = parseFloat(document.getElementById('input-lat').value);
  const lng = parseFloat(document.getElementById('input-lng').value);
  const radius = parseFloat(document.getElementById('input-radius').value);
  alert(`Fence set at (${lat}, ${lng}) with radius ${radius} meters.`);
});
