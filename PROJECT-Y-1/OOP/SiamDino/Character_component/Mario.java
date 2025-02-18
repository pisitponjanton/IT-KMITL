package Character_component;

import AllMom.MomCharacter;

public class Mario extends MomCharacter {
    public Mario() {
        super(200, 200, 600, 540, "mario");
        super.startAnimation();
        super.startMove();
    }
}
