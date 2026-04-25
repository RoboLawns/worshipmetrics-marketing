export interface RoleSectionGroup {
  heading: string;
  items: string[];
}

export interface AVTeamRole {
  slug: string;
  title: string;
  subtitle: string;
  accentColor: string;
  oneLine: string;
  metaTitle: string;
  metaDescription: string;
  heroHeading: string;
  heroSubheading: string;
  intercomPriority: string;
  skillLevel: string;
  typicalAge: string;
  roleSentence: string;
  whoIntro: string;
  whoTraits: string[];
  youthAngle: string;
  panelIntro: string;
  controls: string[];
  behavior: string;
  techReassurance: string;
  compatibilityIntro: string;
  compatibilityGroups: RoleSectionGroup[];
  tabletBody: string;
  intercomBody: string;
  teamPlacement: string;
}

export const avTeamRoles: AVTeamRole[] = [
  {
    slug: "service-director",
    title: "Service Director",
    subtitle: "The Quarterback",
    accentColor: "#1E3A5F",
    oneLine: "Calls the show and keeps every role moving together.",
    metaTitle: "Service Director | The Quarterback of Your AV Team",
    metaDescription:
      "The Service Director calls the show on Sunday morning. One tap advances cues, moves the service forward, and keeps the whole team synchronized.",
    heroHeading: "The Service Director",
    heroSubheading:
      "The person who calls the show. One tap moves the service forward so cameras, lyrics, audio, lighting, and the team stay together.",
    intercomPriority: "Always active",
    skillLevel: "Advanced",
    typicalAge: "17+ or experienced adult volunteer",
    roleSentence:
      "The Service Director calls the show. They move the service forward, trigger key transitions, and keep the team in sync in real time.",
    whoIntro:
      "This is the senior seat on the team. It usually belongs to your most experienced volunteer, a staff leader, or a student who has grown into real responsibility.",
    whoTraits: [
      "Stay calm when things go off-script",
      "See the big picture while thinking one cue ahead",
      "Communicate clearly under pressure",
      "Enjoy being in charge of something that matters",
      "Earn the team's trust by serving in other seats first",
    ],
    youthAngle:
      "For youth teams, this is the role a teenager grows into after years of serving well in other seats. It gives veteran students a rank worth earning and turns experience into visible leadership.",
    panelIntro:
      "The Director's panel is built around one core idea: one tap, the service moves. It keeps the room from depending on one person juggling five systems by memory.",
    controls: [
      "GO / Next Cue to advance to the next service item",
      "Previous Cue to step back when something needs to reset",
      "Hold for prayer, altar calls, or unscripted moments",
      "Scene buttons for worship, sermon, announcements, and prayer",
      "Fade to Black with a guarded confirm step",
      "Rundown view with a live position marker",
      "Call All push-to-talk to the whole team",
    ],
    behavior:
      "The current cue is highlighted, the next cue is always visible, and the most important controls are oversized for live use. Emergency actions are guarded so the interface stays safe for real Sunday pressure.",
    techReassurance:
      "The Service Director panel runs in any modern web browser on a laptop, phone, or WorshipMetrics Tablet over church Wi-Fi.",
    compatibilityIntro:
      "This is the most integration-heavy role because one cue often needs to coordinate several systems at once.",
    compatibilityGroups: [
      {
        heading: "Works across the major production stack",
        items: [
          "Video mixers like vMix, OBS Studio, Blackmagic ATEM, TriCaster, Livestream Studio, Roland, and Magewell Director Mini",
          "Presentation systems like ProPresenter and PowerPoint",
          "Audio consoles like Behringer X32, X-Air, Soundcraft Ui, and other digital mixers through common control protocols",
          "Lighting consoles from MA Lighting, ChamSys, Obsidian Onyx, Avolites, and ShowCAD",
          "Media playback and recorder systems like Resolume, QLab, Millumin, and HyperDeck",
          "PTZ camera systems from PTZOptics, Panasonic, AIDA, and other VISCA or NDI-capable cameras",
        ],
      },
    ],
    tabletBody:
      "This role works especially well on a tablet because the director can move through cues, view the rundown, and keep the service flowing without being chained to one control surface.",
    intercomBody:
      "The Director always has intercom. This is the seat most likely to be talking because the rest of the team is listening for cues and corrections in real time.",
    teamPlacement:
      "The Director is the senior role. New volunteers usually spend time on Lyrics, Camera, or Recording first, then grow into this seat once they know the shape of a service well enough to lead it.",
  },
  {
    slug: "camera-operator",
    title: "Camera Operator",
    subtitle: "The Shot Framer",
    accentColor: "#2E7D5F",
    oneLine: "Owns one camera with presets, tally, and live framing.",
    metaTitle: "Camera Operator | The Shot Framer",
    metaDescription:
      "The Camera Operator frames one camera with live preview, preset recall, tally awareness, and simple manual control from a tablet.",
    heroHeading: "The Camera Operator",
    heroSubheading:
      "One seat per camera. A live preview, one-tap presets, and simple manual control make this one of the strongest early roles on the team.",
    intercomPriority: "Usually active on the pastor camera",
    skillLevel: "Intermediate",
    typicalAge: "14+",
    roleSentence:
      "The Camera Operator owns one camera. They recall the right shots on cue, make small adjustments, and keep the image clean and ready.",
    whoIntro:
      "Camera is one of the best volunteer seats because it balances real responsibility with a visible, rewarding skill people can improve week after week.",
    whoTraits: [
      "Have a good eye and notice when something looks off",
      "Care about craft and composition",
      "Focus well for an hour at a time",
      "Enjoy the visual side of production",
    ],
    youthAngle:
      "For youth teams, Camera is often where teenagers spend the most time because they can see their work immediately. That visible mastery is deeply motivating and creates proud ownership quickly.",
    panelIntro:
      "The Camera Operator panel is built around one feature that changes everything for a volunteer: a live preview inside the panel itself.",
    controls: [
      "Live video preview tile for this camera",
      "Preset buttons for wide, pastor, worship lead, drummer, band wide, and congregation shots",
      "Joystick widget for pan and tilt",
      "Zoom fader for smooth adjustment",
      "Speed toggle for live and off-air movement",
      "Tally indicator for live, preview, or idle state",
      "Optional intercom push-to-talk",
    ],
    behavior:
      "Preset buttons are labeled in plain English, on-air moves can be guarded while tally is red, and camera standards stay consistent because admins maintain the presets instead of each volunteer improvising them.",
    techReassurance:
      "The camera panel runs in any browser on a laptop, phone, or WorshipMetrics Tablet over church Wi-Fi.",
    compatibilityIntro:
      "This role is designed to work with the PTZ camera systems churches already own.",
    compatibilityGroups: [
      {
        heading: "Supports the common church PTZ stack",
        items: [
          "PTZOptics, Panasonic UE, AIDA, and Blackmagic camera control workflows",
          "VISCA-over-IP cameras from brands like Sony, JVC, Lumens, BirdDog, and Marshall",
          "NDI-capable PTZ systems where live preview and control belong together",
          "Tally feedback from the major church switcher environments including vMix, OBS, ATEM, TriCaster, Livestream Studio, and Roland",
        ],
      },
    ],
    tabletBody:
      "This role works well on a tablet because volunteers can hold the panel in their lap, see the live shot, and stay in position without a separate monitor.",
    intercomBody:
      "Intercom is optional per camera seat. Many churches keep at least one camera hot so the Director can coach movement in real time when the pastor or worship leader shifts position.",
    teamPlacement:
      "Camera is a strong second role after Lyrics. It teaches volunteers to think visually about the service and often becomes the path toward the Director seat later.",
  },
  {
    slug: "audio-engineer",
    title: "Audio Engineer",
    subtitle: "The Ears",
    accentColor: "#8B4A6F",
    oneLine: "Keeps the room mix and stream mix clean and steady.",
    metaTitle: "Audio Engineer | The Ears of Your Service",
    metaDescription:
      "The Audio Engineer keeps the mix clean for the room and the stream with scene recalls, key mute controls, and broadcast awareness.",
    heroHeading: "The Audio Engineer",
    heroSubheading:
      "The person with the best ears on the team. Pastor mic control, scene recalls, and stream mix awareness stay visible and close at hand.",
    intercomPriority: "Recommended when staffed as its own seat",
    skillLevel: "Intermediate to advanced",
    typicalAge: "16+",
    roleSentence:
      "The Audio Engineer protects the mix by muting at the right moments, recalling the right scenes, and keeping both the room and the stream sounding clean.",
    whoIntro:
      "Audio is where attention to detail matters most. Great audio disappears into the service. Bad audio becomes the service everyone remembers.",
    whoTraits: [
      "Have a genuinely good ear for music and balance",
      "Focus well for long stretches",
      "Care about precision and timing",
      "Enjoy technical systems that reward practice",
    ],
    youthAngle:
      "For youth teams, audio often attracts students with musical instincts or worship-band experience. It is a deeper skill track that can grow into serious expertise and even future careers.",
    panelIntro:
      "The Audio Engineer panel is designed around the controls that matter most in a service, especially the mute and scene actions volunteers reach for constantly.",
    controls: [
      "Pastor mic mute and unmute as the dominant control",
      "Worship leader mute and band mute groups",
      "Scene recall buttons for worship, sermon, and video playback",
      "Broadcast master fader and live metering for the stream send",
      "Guarded phantom power and backstage talkback controls",
      "Intercom push-to-talk for coordination",
    ],
    behavior:
      "Live mute state reflects the actual mixer, scene recalls are guarded, and stream metering stays visible so the online audience is not an afterthought.",
    techReassurance:
      "The audio panel runs in any browser on any device connected to church Wi-Fi, including the WorshipMetrics Tablet.",
    compatibilityIntro:
      "Audio works best when it meets churches where they already are, whether they run a common digital console or need a lighter bridge into control.",
    compatibilityGroups: [
      {
        heading: "Strong fit for common digital consoles",
        items: [
          "Behringer X32 and X-Air systems",
          "Soundcraft Ui series mixers",
          "Other digital consoles through standard control methods like OSC, MIDI, HTTP, or websocket bridges when needed",
        ],
      },
      {
        heading: "If your church still runs analog",
        items: [
          "Broadcast-side controls can still live inside your streaming software workflow",
          "The role structure still helps the team even when the hardware layer is simpler",
        ],
      },
    ],
    tabletBody:
      "A tablet keeps the most important audio actions visible and accessible without forcing a volunteer to learn the entire console interface at once.",
    intercomBody:
      "Intercom is strongly recommended when Audio is its own seat. The engineer needs to hear upcoming transitions and the Director needs fast feedback when something fails.",
    teamPlacement:
      "Audio is usually a deeper-skill role than Camera or Lyrics. Volunteers often spend time in other seats first, then move here as their confidence and judgment grow.",
  },
  {
    slug: "lyrics-operator",
    title: "Lyrics Operator",
    subtitle: "The Story Keeper",
    accentColor: "#B86A2E",
    oneLine: "Advances lyrics, sermon slides, and lower-thirds on cue.",
    metaTitle: "Lyrics Operator | The Story Keeper",
    metaDescription:
      "The Lyrics Operator advances song slides, sermon graphics, and lower-thirds in real time. It is one of the best first seats for a new volunteer.",
    heroHeading: "The Lyrics Operator",
    heroSubheading:
      "Advance slides, cue sermon graphics, and keep the words moving. This is the best first seat for brand-new volunteers and younger students.",
    intercomPriority: "Usually active",
    skillLevel: "Beginner",
    typicalAge: "12+",
    roleSentence:
      "The Lyrics Operator runs the words: worship lyrics, sermon slides, lower-thirds, scripture references, and countdown moments.",
    whoIntro:
      "Lyrics is the front door for most teams because a new volunteer can contribute visibly within minutes and leave the service feeling like they truly helped.",
    whoTraits: [
      "Stay attentive to pace and timing",
      "Enjoy following along with music and reading",
      "Handle responsibility without needing the spotlight",
      "Want to help right away",
    ],
    youthAngle:
      "For youth teams, this is where most students should start. A 12- or 13-year-old can learn the three most important buttons quickly, get a first-week win, and begin to see themselves as part of the team.",
    panelIntro:
      "The Lyrics panel is designed around one thing above all: making the Next Slide button impossible to miss.",
    controls: [
      "Oversized Next Slide button in a consistent position",
      "Previous Slide and Clear controls",
      "Song library and active song context",
      "Scripture quick-recall and lower-third triggers",
      "Countdown timers and stage display toggle",
      "Intercom push-to-talk",
    ],
    behavior:
      "Next Slide is huge and always where the volunteer expects it. Current slide state stays visible, risky actions are guarded, and the panel is designed so a beginner can contribute without getting lost.",
    techReassurance:
      "The Lyrics panel runs in any web browser and works especially well on a tablet a volunteer can hold in their lap.",
    compatibilityIntro:
      "The volunteer experience stays simple even when churches run different presentation software underneath.",
    compatibilityGroups: [
      {
        heading: "Fits the common church presentation stack",
        items: [
          "ProPresenter workflows through its network controls",
          "PowerPoint and other presentation software through standard remote methods",
          "A familiar volunteer interface regardless of what software the church already uses",
        ],
      },
    ],
    tabletBody:
      "This role is perfect for a tablet because a volunteer can sit wherever they have the clearest view of the stage without needing a complicated booth station.",
    intercomBody:
      "Intercom is usually active for Lyrics because slide timing corrections are one of the most common real-time coaching moments in a live service.",
    teamPlacement:
      "Lyrics is the front door. New volunteers start here, learn the rhythm of a service, and then graduate into Camera or another seat after a season or two.",
  },
  {
    slug: "stream-operator",
    title: "Stream Operator",
    subtitle: "The Broadcaster",
    accentColor: "#C93A3A",
    oneLine: "Owns the online service from countdown to closing screen.",
    metaTitle: "Stream Operator | The Broadcaster",
    metaDescription:
      "The Stream Operator owns the online service from start to finish with stream health monitoring, broadcast scenes, and recording control.",
    heroHeading: "The Stream Operator",
    heroSubheading:
      "The person responsible for the online service. Start the stream, monitor health, run broadcast-specific graphics, and catch problems before the online congregation feels them.",
    intercomPriority: "Strongly recommended",
    skillLevel: "Intermediate",
    typicalAge: "15+",
    roleSentence:
      "The Stream Operator owns everything the online congregation sees. They keep the stream healthy, manage broadcast-specific moments, and catch problems early.",
    whoIntro:
      "The Stream Operator becomes its own seat when the online congregation matters enough to deserve focused care instead of being folded into everything else.",
    whoTraits: [
      "Stay calm when health meters start blinking red",
      "Enjoy troubleshooting and technical systems",
      "Care about the online congregation as a real audience",
      "Like being the bridge between in-room and online",
    ],
    youthAngle:
      "For youth teams, this role is a strong fit for students who already understand streaming from gaming, YouTube, or social platforms. It turns a hobby into real ministry and real technical experience.",
    panelIntro:
      "The Stream Operator panel is designed around one worst-case scenario: a dropping stream must be noticed immediately.",
    controls: [
      "Start and stop stream controls with guardrails",
      "Always-visible stream health indicators",
      "Broadcast scene buttons for pre-service, live, and post-service states",
      "Online-specific lower-thirds and prompts",
      "Chat monitor access",
      "Recording control and intercom push-to-talk",
    ],
    behavior:
      "Health data never hides behind tabs. Warning thresholds escalate visually, risky actions are guarded, and broadcast state stays obvious at a glance.",
    techReassurance:
      "The stream panel runs in any browser on a laptop, phone, or WorshipMetrics Tablet over the church Wi-Fi.",
    compatibilityIntro:
      "This role is built to sit on top of the streaming environments churches already use.",
    compatibilityGroups: [
      {
        heading: "Works with the major church streaming stack",
        items: [
          "vMix, OBS Studio, Blackmagic ATEM, TriCaster, Livestream Studio, and Magewell Director Mini workflows",
          "Local recording systems like HyperDeck",
          "Cloud and hardware encoder paths where start-stop and health signals need to stay visible to the operator",
          "Multi-destination streaming workflows for YouTube, Facebook, and website players",
        ],
      },
    ],
    tabletBody:
      "A tablet means the Stream Operator can sit with the team and still watch stream health without being chained to the streaming PC.",
    intercomBody:
      "Intercom is strongly recommended. The Stream Operator needs the Director's timing cues, and the Director needs instant warning when the stream becomes unstable.",
    teamPlacement:
      "This role often becomes the Director-in-training seat. Volunteers who master the stream seat learn both service flow and technical broadcast judgment.",
  },
  {
    slug: "lighting-operator",
    title: "Lighting Operator",
    subtitle: "The Atmosphere",
    accentColor: "#7A4AA8",
    oneLine: "Shapes the room with cue-based looks and smooth transitions.",
    metaTitle: "Lighting Operator | The Atmosphere",
    metaDescription:
      "The Lighting Operator shapes the room with cue-based looks, safe fades, and transitions that help the service feel intentional.",
    heroHeading: "The Lighting Operator",
    heroSubheading:
      "Sets the mood of the room with a single tap. Worship, sermon, prayer, and altar call each get a look that changes smoothly instead of abruptly.",
    intercomPriority: "Optional",
    skillLevel: "Intermediate",
    typicalAge: "14+",
    roleSentence:
      "The Lighting Operator shapes the room with pre-built looks, safe overrides, and smooth transitions between moments.",
    whoIntro:
      "Lighting looks technical from the outside, but the work is deeply artistic. This role is visual design during a live service.",
    whoTraits: [
      "Have a visual or artistic sensibility",
      "Notice when a room feels right or doesn't",
      "Enjoy the performance side of production",
      "Feel comfortable making small judgment calls live",
    ],
    youthAngle:
      "For youth teams, lighting attracts creative students who want to feel like artists, not just operators. It gives them a real aesthetic role in the service.",
    panelIntro:
      "The Lighting Operator panel is designed around one principle: looks should crossfade, not snap.",
    controls: [
      "Look buttons for pre-service, worship, sermon, prayer, altar call, announcements, and post-service",
      "Manual house lights and stage wash faders",
      "Emergency blackout with a confirm guard",
      "Optional intercom push-to-talk",
    ],
    behavior:
      "Looks crossfade over programmed durations, safe ranges keep volunteers from making room-breaking mistakes, and the visual language stays consistent even when the house style evolves.",
    techReassurance:
      "The lighting panel runs in any browser on a laptop, phone, or WorshipMetrics Tablet over the church Wi-Fi.",
    compatibilityIntro:
      "This role scales from a real console-driven rig down to simple room-light control.",
    compatibilityGroups: [
      {
        heading: "Works with major lighting environments",
        items: [
          "MA Lighting, Obsidian Onyx, Avolites, ChamSys, and ShowCAD workflows",
          "Universal lighting protocols like Art-Net, sACN, and OSC where a church's specific console needs a bridge",
          "Simpler dimmer or smart-switch style control for churches without a full lighting rig",
        ],
      },
    ],
    tabletBody:
      "A tablet is useful here because volunteers can walk the room during setup or rehearsal and judge the look from where people actually sit.",
    intercomBody:
      "Intercom is optional. Larger churches with a dedicated lighting seat often use it, while smaller teams often fold this role into the Director's responsibilities.",
    teamPlacement:
      "Lighting is a creative-track role. Volunteers who love it often stay in it for years and become the people who shape how the room feels.",
  },
  {
    slug: "recording-archivist",
    title: "Recording / Archivist",
    subtitle: "The Historian",
    accentColor: "#4A6B7A",
    oneLine: "Makes sure every service is captured and useful afterward.",
    metaTitle: "Recording / Archivist | The Historian",
    metaDescription:
      "The Recording / Archivist makes sure every service is captured cleanly for archive, editing, and content reuse.",
    heroHeading: "The Recording / Archivist",
    heroSubheading:
      "The insurance policy. Make sure every service is being recorded cleanly, mark key moments for the edit team, and save moments worth clipping later.",
    intercomPriority: "Optional or listen-only",
    skillLevel: "Beginner to intermediate",
    typicalAge: "13+",
    roleSentence:
      "The Recording / Archivist makes sure the service is actually being captured, marked, and handed off well for the week that follows.",
    whoIntro:
      "This role is easy to underestimate. It is not the loudest seat, but it may save Monday morning more often than any other.",
    whoTraits: [
      "Be meticulous and detail-oriented",
      "Enjoy organizing and labeling things",
      "Pay attention without needing to be at the center of the action",
      "Like being the reason the post-service work goes smoothly",
    ],
    youthAngle:
      "For youth teams, this is a strong fit for quieter or more introverted students who want meaningful responsibility without the pressure of live decision-making every second.",
    panelIntro:
      "The Recording panel is dominated by one question: is this actually being captured? That answer should never be more than a glance away.",
    controls: [
      "Start and stop recording across configured destinations",
      "Recording health with per-destination status and storage remaining",
      "Chapter markers for worship, sermon, altar call, and custom moments",
      "Voice-friendly notes for edit and content teams",
      "Snapshot frame capture for weekly recap or social use",
      "Optional intercom push-to-talk",
    ],
    behavior:
      "Recording health dominates the screen, markers feed directly into the service record, storage warnings escalate clearly, and snapshots save valuable context for the week after the service.",
    techReassurance:
      "The recording panel runs in any browser on a laptop, phone, or WorshipMetrics Tablet over the church Wi-Fi.",
    compatibilityIntro:
      "This role bridges the live service and the week-after workflow, which makes it especially valuable for content-minded churches.",
    compatibilityGroups: [
      {
        heading: "Works with common recording paths",
        items: [
          "vMix and OBS recording workflows",
          "HyperDeck and other network-addressable recorder environments",
          "Camera-mounted or external recording systems where churches need oversight, not guesswork",
          "Service metadata and marker workflows that make Monday editing and clipping easier",
        ],
      },
    ],
    tabletBody:
      "A tablet lets this volunteer keep capture health, markers, and notes in one place without demanding a full booth workstation.",
    intercomBody:
      "Intercom is optional here and often becomes listen-only when the church has limited hot seats. The role still matters even when it is quieter.",
    teamPlacement:
      "Recording is a great entry seat for detail-oriented students and a strong support seat for veterans who want to serve without carrying the full live pressure of the Director chair.",
  },
];

export const avTeamHub = {
  title: "Build Your AV Team",
  heroHeading: "You don't need more gear. You need a team.",
  heroSubheading:
    "WorshipMetrics Pro gives every church an AV Club out of the box: seven volunteer roles, seven prebuilt control panels, and a structure that turns your media ministry into a thriving youth ministry.",
  metaDescription:
    "WorshipMetrics Pro gives your church a complete AV team structure: seven prebuilt volunteer roles, each with its own control panel, training path, and place on the team.",
};

export const avTeamRoleMap = Object.fromEntries(avTeamRoles.map((role) => [role.slug, role]));

export function getAVTeamRole(slug: string) {
  return avTeamRoleMap[slug];
}

export function getAVTeamRoleIndex(slug: string) {
  return avTeamRoles.findIndex((role) => role.slug === slug);
}

export function getAVTeamNeighbors(slug: string) {
  const index = getAVTeamRoleIndex(slug);
  return {
    previous: index > 0 ? avTeamRoles[index - 1] : null,
    current: index >= 0 ? avTeamRoles[index] : null,
    next: index >= 0 && index < avTeamRoles.length - 1 ? avTeamRoles[index + 1] : null,
  };
}
