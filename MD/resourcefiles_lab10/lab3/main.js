function init() {
    const scene = new THREE.Scene();
    const gui = new dat.GUI();

    // ---------- Materials ----------
    const sphereMaterial = getMaterial('rgb(255,245,245)');
    const planeMaterial = getMaterial('rgb(255,255,255)');

    // ---------- Objects ----------
    const sphere = getSphere(sphereMaterial, 1, 24);
    sphere.position.y = 1; // วางบน plane

    const plane = getPlane(planeMaterial, 30);
    plane.rotation.x = Math.PI / 2;

    // ---------- Lights ----------
    const spotLight = getSpotLight(2, 'rgb(255,220,180)');
    spotLight.position.set(-5, 4, -4);

    // ---------- Texture Loader ----------
    const loader = new THREE.TextureLoader();
    sphereMaterial.map = loader.load('/assets/textures/concrete.jpg');
    planeMaterial.map = loader.load('/assets/textures/checkerboard.jpg');

    // ---------- GUI ----------
    const lightFolder = gui.addFolder('Light');
    lightFolder.add(spotLight, 'intensity', 0, 10);
    lightFolder.add(spotLight.position, 'x', -10, 10);
    lightFolder.add(spotLight.position, 'y', 0, 10);
    lightFolder.add(spotLight.position, 'z', -10, 10);

    const matFolder = gui.addFolder('Materials');
    matFolder.add(sphereMaterial, 'roughness', 0, 1);
    matFolder.add(planeMaterial, 'roughness', 0, 1);
    matFolder.add(sphereMaterial, 'metalness', 0, 1);
    matFolder.add(planeMaterial, 'metalness', 0, 1);
    matFolder.open();

    // ---------- Camera ----------
    const camera = new THREE.PerspectiveCamera(
        45,
        window.innerWidth / window.innerHeight,
        1,
        1000
    );
    camera.position.set(-2, 7, 7);
    camera.lookAt(new THREE.Vector3(0, 0, 0));

    // ---------- Renderer ----------
    const renderer = new THREE.WebGLRenderer();
    renderer.setSize(window.innerWidth, window.innerHeight);
    renderer.shadowMap.enabled = true;
    document.getElementById("webgl").appendChild(renderer.domElement);

    // ---------- Controls ----------
    const controls = new THREE.OrbitControls(camera, renderer.domElement);

    // ---------- Add to Scene ----------
    scene.add(sphere);
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

function getMaterial(color) {
    return new THREE.MeshStandardMaterial({
        color: color || 'rgb(255,255,255)'
    });
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
