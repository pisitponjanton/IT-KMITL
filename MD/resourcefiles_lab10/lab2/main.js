function init() {
    const scene = new THREE.Scene();
    const gui = new dat.GUI();

    // ---------- Objects ----------
    const plane = getPlane(30);
    plane.rotation.x = Math.PI / 2;

    const boxGrid = getBoxGrid(10, 1.5);

    // SpotLight + Sphere marker
    const spotLight = getSpotLight(2);
    spotLight.position.set(3, 4, 5);
    const sphere = getSphere(0.1);
    spotLight.add(sphere);

    // ---------- Camera ----------
    const camera = new THREE.PerspectiveCamera(
        50,
        window.innerWidth / window.innerHeight,
        1,
        1000
    );
    camera.position.set(5, 7, 10);
    camera.lookAt(new THREE.Vector3(0, 0, 0));

    // ---------- Renderer ----------
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.setClearColor('rgb(120,120,120)');
    renderer.shadowMap.enabled = true;
    document.getElementById("webgl").appendChild(renderer.domElement);

    // ---------- Controls ----------
    const controls = new THREE.OrbitControls(camera, renderer.domElement);

    // ---------- Add to Scene ----------
    scene.add(plane);
    scene.add(boxGrid);
    scene.add(spotLight);

    // ---------- GUI ----------
    gui.add(spotLight, 'intensity', 0, 10);
    gui.add(spotLight.position, 'x', -20, 20);
    gui.add(spotLight.position, 'y', 0, 20);
    gui.add(spotLight.position, 'z', -20, 20);
    gui.add(spotLight, 'penumbra', 0, 1);

    // ---------- Render Loop ----------
    update(renderer, scene, camera, controls);
}

// ---------- Helpers ----------
function getBox(w, h, d) {
    const geometry = new THREE.BoxGeometry(w, h, d);
    const material = new THREE.MeshPhongMaterial({ color: 'rgb(0,255,0)' });
    const mesh = new THREE.Mesh(geometry, material);
    mesh.castShadow = true;
    return mesh;
}

function getBoxGrid(amount, separation) {
    const group = new THREE.Group();
    for (let i = 0; i < amount; i++) {
        for (let j = 0; j < amount; j++) {
            const box = getBox(1, 1, 1);
            box.position.set(i * separation, 0.5, j * separation);
            group.add(box);
        }
    }
    group.position.x = -(separation * (amount - 1)) / 2;
    group.position.z = -(separation * (amount - 1)) / 2;
    return group;
}

function getPlane(size) {
    const geometry = new THREE.PlaneGeometry(size, size);
    const material = new THREE.MeshPhongMaterial({ color: 'rgb(200,200,200)', side: THREE.DoubleSide });
    const mesh = new THREE.Mesh(geometry, material);
    mesh.receiveShadow = true;
    return mesh;
}

function getSphere(size) {
    const geometry = new THREE.SphereGeometry(size, 24, 24);
    const material = new THREE.MeshBasicMaterial({ color: 'rgb(0,0,0)' });
    const mesh = new THREE.Mesh(geometry, material);
    return mesh;
}

function getSpotLight(intensity) {
    const light = new THREE.SpotLight(0xffffff, intensity);
    light.castShadow = true;
    light.shadow.bias = 0.001;
    light.shadow.mapSize.width = 2048;
    light.shadow.mapSize.height = 2048;
    return light;
}

function update(renderer, scene, camera, controls) {
    controls.update();
    renderer.render(scene, camera);
    requestAnimationFrame(function () {
        update(renderer, scene, camera, controls);
    });
}

init();
