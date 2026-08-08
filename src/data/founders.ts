const R2 = "https://pub-a4845709a76642e7943bcb8b80677531.r2.dev/main";

export type Founder = {
  name: string;
  role: string;
  photo: string;
  /** One short line for compact placements (strips, cards). */
  line: string;
  /** Number of children — the detail behind why the AV Club matters to us. */
  kids: number;
};

export const founders: Founder[] = [
  {
    name: "Paul Richards",
    role: "Educator & Onboarding",
    photo: `${R2}/paul.jpg`,
    line: "Twelve years helping churches stream, at PTZOptics. Author of Helping Your Church Live Stream.",
    kids: 3,
  },
  {
    name: "Seth Haberman",
    role: "CTO & Digital Pastor",
    photo: `${R2}/homepage/Seth%20Haberman.jpeg`,
    line: "Worship leader, camera operator, and the engineer who builds what he has already had to run.",
    kids: 5,
  },
  {
    name: "Rev. Andrew Esqueda",
    role: "Pastor & Visionary",
    photo: "/legacy-images/rev-andrew-esqueda.jpeg",
    line: "An active senior pastor with a real congregation and a real Sunday to get through every week.",
    kids: 3,
  },
];

/** Eleven — the number behind why we care so much about the AV Club. */
export const totalKids = founders.reduce((sum, f) => sum + f.kids, 0);
