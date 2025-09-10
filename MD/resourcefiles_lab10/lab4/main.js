function init() {
    const scene = new THREE.Scene();
    const gui = new dat.GUI();

    // ---------- Materials ----------
    const sphereMaterial = getMaterial();
    const planeMaterial = getMaterial();

    // ---------- Objects ----------
    const sphereGrid = getSphereGrid(10, 1.5, sphereMaterial);
    const plane = getPlane(planeMaterial, 40);
    plane.rotation.x = Math.PI / 2;

    // ---------- Lights ----------
    const spotLight = getSpotLight(2, 'rgb(255,220,180)');
    spotLight.position.set(-10, 15, 10);

    // ---------- Texture Loader ----------
    const loader = new THREE.TextureLoader();
    sphereMaterial.map = loader.load('/assets/textures/concrete.jpg');
    planeMaterial.map = loader.load('/assets/textures/checkerboard.jpg');

    // ---------- GUI ----------
    const lightFolder = gui.addFolder('Light');
    lightFolder.add(spotLight, 'intensity', 0, 10);
    lightFolder.add(spotLight.position, 'x', -20, 20);
    lightFolder.add(spotLight.position, 'y', 0, 20);
    lightFolder.add(spotLight.position, 'z', -20, 20);

    const matFolder = gui.addFolder('Materials');
    matFolder.add(sphereMaterial, 'roughness', 0, 1);
    matFolder.add(sphereMaterial, 'metalness', 0, 1);
    matFolder.add(planeMaterial, 'roughness', 0, 1);
    matFolder.add(planeMaterial, 'metalness', 0, 1);

    // ---------- Camera ----------
    const camera = new THREE.PerspectiveCamera(
        45,
        window.innerWidth / window.innerHeight,
        1,
        1000
    );
    camera.position.set(15, 20, 25);
    camera.lookAt(new THREE.Vector3(0, 0, 0));

    // ---------- Renderer ----------
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.shadowMap.enabled = true;
    document.getElementById("webgl").appendChild(renderer.domElement);

    // ---------- Controls ----------
    const controls = new THREE.OrbitControls(camera, renderer.domElement);

    // ---------- Add to Scene ----------
    scene.add(sphereGrid);
    scene.add(plane);
    scene.add(spotLight);

    // ---------- Loop ----------
    update(renderer, scene, camera, controls);
}

// ---------- Helpers ----------
function getSphere(material, size, segments) {
    const geometry = new THREE.SphereGeometry(size, segments, segments);
    const mesh = new THREE.Mesh(geometry, material);
    mesh.castShadow = true;
    return mesh;
}

function getSphereGrid(amount, separation, material) {
    const group = new THREE.Group();
    for (let i = 0; i < amount; i++) {
        for (let j = 0; j < amount; j++) {
            const sphere = getSphere(material, 0.5, 24);
            sphere.position.set(i * separation, 0.5, j * separation);
            group.add(sphere);
        }
    }
    group.position.x = -(separation * (amount - 1)) / 2;
    group.position.z = -(separation * (amount - 1)) / 2;
    return group;
}

function getMaterial() {
    return new THREE.MeshStandardMaterial({ color: 'rgb(255,255,255)' });
}

function getPlane(material, size) {
    const geometry = new THREE.PlaneGeometry(size, size);
    material.side = THREE.DoubleSide;
    const mesh = new THREE.Mesh(geometry, material);
    mesh.receiveShadow = true;
    return mesh;
}

function getSpotLight(intensity, color) {
    const light = new THREE.SpotLight(color || 0xffffff, intensity);
    light.castShadow = true;
    light.penumbra = 0.5;
    light.shadow.mapSize.width = 2048;
    light.shadow.mapSize.height = 2048;
    light.shadow.bias = 0.001;
    return light;
}

function update(renderer, scene, camera, controls) {
    controls.update();
    renderer.render(scene, camera);
    requestAnimationFrame(() => update(renderer, scene, camera, controls));
}

init();
