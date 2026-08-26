export interface RoleSectionGroup {
  heading: string;
  items: string[];
}

export interface AVTeamRole {
  slug: string;
  title: string;
  /** Role portrait shown on the role page, the carousel cards, and the AV Club page. */
  image: string;
  subtitle: string;
  accentColor: string;
  oneLine: string;
  metaTitle: string;
  metaDescription: string;
  heroHeading: string;
  heroSubheading: string;
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
  teamPlacement: string;
}

export const avTeamRoles: AVTeamRole[] = [
  {
    slug: "service-director",
    image: "/images/roles/av-role-service-director.jpg",
    title: "Service Director",
    subtitle: "The Quarterback",
    accentColor: "#1E3A5F",
    oneLine: "Calls the show and keeps every role moving together.",
    metaTitle: "Service Director | The Quarterback of Your AV Team",
    metaDescription:
      "The Service Director calls the show on Sunday morning. They run the service plan, keep every seat looking at the same moment, and lead the team in real time.",
    heroHeading: "The Service Director",
    heroSubheading:
      "The person who calls the show. They run the service plan live, so cameras, lyrics, audio, and the rest of the team stay on the same moment together.",
    skillLevel: "Advanced",
    typicalAge: "17+ or experienced adult volunteer",
    roleSentence:
      "The Service Director calls the show. They move the service forward, call the transitions, and keep the team in sync in real time.",
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
      "The Director works from the live service plan. Every item and cue for the morning is in one rundown, the current position is always visible, and the whole team is looking at the same plan — so the room stops depending on one person juggling five systems by memory.",
    controls: [
      "The live service plan, with the current item highlighted and the next one always visible",
      "Seventeen plan item types and six cue types, so the run sheet reflects how your church actually does a service",
      "Present triggers that can fire cues at vMix, OBS, ProPresenter, QLab, Resolume, and more as the service moves",
      "Team Chat for the calls, confirmations, and quick questions that used to live on a headset",
      "Serving assignments, so the Director knows exactly who is in every seat this morning",
    ],
    behavior:
      "The plan is built before Sunday and run live on Sunday. The Director calls the moments; every seat sees the same rundown; and when something goes off-script, the plan and the chat keep the whole team recoverable.",
    techReassurance:
      "The service plan and Team Chat run in any modern web browser on a laptop, phone, or WorshipMetrics Tablet over church Wi-Fi.",
    compatibilityIntro:
      "This seat leads people more than machines — but the systems in the room still follow along.",
    compatibilityGroups: [
      {
        heading: "Works across the production stack",
        items: [
          "Present can fire outbound cues over OSC, RossTalk, MIDI, or HTTP, with ready-made presets for vMix, OBS, ProPresenter, QLab, Resolume, Companion, disguise, Behringer X32/M32, and Q-SYS",
          "vMix gets a full remote switcher panel; OBS gets remote scene, stream, and recording control",
          "The service plan syncs with Planning Center, so the run sheet matches what the worship team already built",
          "AV health monitoring shows the Director whether every critical device in the room is up before the countdown ends",
        ],
      },
    ],
    tabletBody:
      "This role works especially well on a tablet because the Director can carry the rundown, watch the room, and keep the service flowing without being chained to one desk.",
    teamPlacement:
      "The Director is the senior role. New volunteers usually spend time on Lyrics, Camera, or Recording first, then grow into this seat once they know the shape of a service well enough to lead it.",
  },
  {
    slug: "camera-operator",
    image: "/images/roles/av-role-camera-operator.jpg",
    title: "Camera Operator",
    subtitle: "The Shot Framer",
    accentColor: "#2E7D5F",
    oneLine: "Owns one camera with presets and live framing.",
    metaTitle: "Camera Operator | The Shot Framer",
    metaDescription:
      "The Camera Operator frames the shots. With PTZ presets and smooth control through Tech Manager, they recall the right shot on cue and keep the image clean.",
    heroHeading: "The Camera Operator",
    heroSubheading:
      "One seat that owns the shots. Preset recall and smooth PTZ control make this one of the strongest early roles on the team.",
    skillLevel: "Intermediate",
    typicalAge: "14+",
    roleSentence:
      "The Camera Operator owns the cameras. They recall the right shots on cue, make small adjustments, and keep the image clean and ready.",
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
      "Tech Manager gives this seat real PTZ control: saved presets for the standard shots, smooth pan-tilt-zoom moves, and a command watchdog that stops a runaway camera before the congregation sees it.",
    controls: [
      "Preset recall for the shots your church uses every week — wide, pastor, worship lead, band, congregation",
      "Pan, tilt, and zoom control over VISCA-over-IP (TCP 52381)",
      "A command watchdog that supersedes stale moves, so a camera never keeps drifting after the operator lets go",
      "Camera health on the AV monitoring dashboard, so a dropped camera is noticed before the service starts",
      "The service plan alongside, so the operator always knows which moment is coming next",
    ],
    behavior:
      "Presets are set up once by the tech manager and recalled by name, so camera standards stay consistent instead of each volunteer improvising them — and a new operator can land the right shot in week one.",
    techReassurance:
      "PTZ control runs through Tech Manager on the booth PC your church already owns. The service plan and Team Chat follow the operator on any browser or tablet.",
    compatibilityIntro:
      "This role is designed to work with the PTZ camera systems churches already own.",
    compatibilityGroups: [
      {
        heading: "Supports the common church PTZ stack",
        items: [
          "VISCA-over-IP cameras, including PTZOptics and the wide family of VISCA-compatible PTZ brands",
          "BirdDog PTZ cameras",
          "A device catalog with factory port maps for the common church camera models, so the wiring is documented before the first preset is saved",
        ],
      },
    ],
    tabletBody:
      "A tablet keeps the service plan and team chat in the operator's lap, so they can stay in position and stay in sync without a second monitor.",
    teamPlacement:
      "Camera is a strong second role after Lyrics. It teaches volunteers to think visually about the service and often becomes the path toward the Director seat later.",
  },
  {
    slug: "audio-engineer",
    image: "/images/roles/av-role-audio-engineer.jpg",
    title: "Audio Engineer",
    subtitle: "The Ears",
    accentColor: "#8B4A6F",
    oneLine: "Keeps the room mix and stream mix clean and steady.",
    metaTitle: "Audio Engineer | The Ears of Your Service",
    metaDescription:
      "The Audio Engineer keeps the mix clean for the room and the stream, with real console control for Behringer X32 and Midas M32 over OSC.",
    heroHeading: "The Audio Engineer",
    heroSubheading:
      "The person with the best ears on the team. They protect the mix for the room and the stream — and WorshipMetrics speaks their console's language.",
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
      "For churches on a Behringer X32 or Midas M32, WorshipMetrics talks to the console directly over OSC — and Present can fire console cues as part of the service, so the moves that happen every single week stop depending on memory.",
    controls: [
      "Direct control for Behringer X32 and Midas M32 over OSC",
      "Present protocol presets that can send console cues alongside lyrics and slides",
      "The console documented on the Signal Map, with every input and output labeled",
      "Console health on the AV monitoring dashboard, so a powered-off or unreachable mixer is caught early",
      "The service plan alongside, so the engineer sees the sermon handoff coming before it arrives",
    ],
    behavior:
      "The console keeps doing what it does best. WorshipMetrics adds the connective tissue: documented wiring, monitored health, and cues that arrive on time.",
    techReassurance:
      "Console control runs from the production computer in the booth. The service plan and Team Chat follow the engineer on any browser or tablet over church Wi-Fi.",
    compatibilityIntro:
      "Audio works best when it meets churches where they already are, whether they run a common digital console or something simpler.",
    compatibilityGroups: [
      {
        heading: "Strong fit for common digital consoles",
        items: [
          "Behringer X32 and Midas M32 over OSC",
          "The wider console world through the device catalog: factory port maps and documentation for the boards churches actually run",
        ],
      },
      {
        heading: "If your church still runs analog",
        items: [
          "The serving structure, the plan, and the documentation still help the team even when the hardware layer is simpler",
          "Stream audio still gets watched through the streaming software's own controls",
        ],
      },
    ],
    tabletBody:
      "A tablet keeps the plan and the team conversation next to the console, so the engineer stays connected to the service without leaving the mix position.",
    teamPlacement:
      "Audio is usually a deeper-skill role than Camera or Lyrics. Volunteers often spend time in other seats first, then move here as their confidence and judgment grow.",
  },
  {
    slug: "lyrics-operator",
    image: "/images/roles/av-role-lyrics-operator.jpg",
    title: "Lyrics Operator",
    subtitle: "The Story Keeper",
    accentColor: "#B86A2E",
    oneLine: "Advances lyrics, sermon slides, and lower-thirds on cue.",
    metaTitle: "Lyrics Operator | The Story Keeper",
    metaDescription:
      "The Lyrics Operator advances song slides, sermon graphics, and lower-thirds in real time with Present. It is one of the best first seats for a new volunteer.",
    heroHeading: "The Lyrics Operator",
    heroSubheading:
      "Advance slides, cue sermon graphics, and keep the words moving with Present. This is the best first seat for brand-new volunteers and younger students.",
    skillLevel: "Beginner",
    typicalAge: "12+",
    roleSentence:
      "The Lyrics Operator runs the words: worship lyrics, sermon slides, lower-thirds, and scripture — everything the congregation reads.",
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
      "This seat runs Present, WorshipMetrics' own presentation software. The service's songs and slides are loaded from the plan, and the volunteer's whole job comes down to one thing done well: the next slide, on time.",
    controls: [
      "Present, with the morning's songs and slides loaded straight from the service plan",
      "A song library with lyrics, keys, and chord charts — plus 94 public-domain hymns included",
      "Scripture slides from six Bible translations",
      "Lower-thirds and a separate stage display output for the band",
      "Imports from ProPresenter 4–7, ChordPro, OpenLyrics, and SongSelect, so the library your church built comes along",
    ],
    behavior:
      "The current slide is always obvious, the next one is queued, and the volunteer advances at the pace of the room. A beginner can contribute without getting lost.",
    techReassurance:
      "Present runs on the production computer your church already owns; the service plan and Team Chat follow the volunteer on any browser or tablet.",
    compatibilityIntro:
      "The volunteer experience stays simple even when churches run other presentation software underneath.",
    compatibilityGroups: [
      {
        heading: "Fits the common church presentation stack",
        items: [
          "Present covers lyrics, slides, scripture, lower-thirds, and stage display out of the box",
          "Churches staying on ProPresenter can import their library into WorshipMetrics for planning, and Present can fire ProPresenter cues over its network protocols",
          "Song imports from ChordPro (.cho, .crd, .chopro), OpenLyrics XML, SongSelect (.usr), ProPresenter 4–7, and plain-text paste",
        ],
      },
    ],
    tabletBody:
      "This role is perfect for a tablet because a volunteer can follow the plan and the chat from wherever they have the clearest view of the stage.",
    teamPlacement:
      "Lyrics is the front door. New volunteers start here, learn the rhythm of a service, and then graduate into Camera or another seat after a season or two.",
  },
  {
    slug: "stream-operator",
    image: "/images/roles/av-role-stream-operator.jpg",
    title: "Stream Operator",
    subtitle: "The Broadcaster",
    accentColor: "#C93A3A",
    oneLine: "Owns the online service from countdown to closing screen.",
    metaTitle: "Stream Operator | The Broadcaster",
    metaDescription:
      "The Stream Operator owns the online service from start to finish with stream health monitoring, remote start-stop for vMix and OBS, and multi-destination streaming.",
    heroHeading: "The Stream Operator",
    heroSubheading:
      "The person responsible for the online service. Start the stream, watch its health in real numbers, and catch problems before the online congregation feels them.",
    skillLevel: "Intermediate",
    typicalAge: "15+",
    roleSentence:
      "The Stream Operator owns everything the online congregation sees. They keep the stream healthy, confirm the recording is rolling, and catch problems early.",
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
      "The Stream Operator's tools are built around one worst-case scenario: a dropping stream must be noticed immediately. Health data comes in every 15 seconds, and the red lines are drawn before Sunday, not after.",
    controls: [
      "Start and stop the stream and the recording in vMix or OBS — from the booth or remotely",
      "Stream health on a 15-second heartbeat, with clear thresholds for when to worry",
      "One feed fanned out to up to 10 destinations — YouTube, Facebook, and more",
      "Live clips up to 10 minutes long, captured while the service is still running",
      "Encoder and network health on the same dashboard, so the cause of a problem is visible next to the symptom",
    ],
    behavior:
      "Health data never hides behind tabs. A stream that stops heartbeating shows an offline badge within 90 seconds, and the operator knows whether the problem is the encoder, the network, or the platform.",
    techReassurance:
      "The stream dashboard runs in any browser on a laptop, phone, or WorshipMetrics Tablet over the church Wi-Fi.",
    compatibilityIntro:
      "This role is built to sit on top of the streaming environments churches already use.",
    compatibilityGroups: [
      {
        heading: "Works with the major church streaming stack",
        items: [
          "vMix, with a full remote switcher panel — preview and program, transitions, overlays, audio, recording, and streaming",
          "OBS Studio, with remote scene switching, stream and recording start-stop, and encoder settings",
          "Blackmagic ATEM switchers, controlled locally in the booth through Tech Manager",
          "Multi-destination streaming to YouTube, Facebook, Twitch, and the major restreaming services",
        ],
      },
    ],
    tabletBody:
      "A tablet means the Stream Operator can sit with the team and still watch stream health without being chained to the streaming PC.",
    teamPlacement:
      "This role often becomes the Director-in-training seat. Volunteers who master the stream seat learn both service flow and technical broadcast judgment.",
  },
  {
    slug: "lighting-operator",
    image: "/images/roles/av-role-lighting-operator.jpg",
    title: "Lighting Operator",
    subtitle: "The Atmosphere",
    accentColor: "#7A4AA8",
    oneLine: "Shapes the room and owns the rig, one look at a time.",
    metaTitle: "Lighting Operator | The Atmosphere",
    metaDescription:
      "The Lighting Operator shapes the room. WorshipMetrics documents and monitors the lighting rig, and Present can fire cues at consoles that listen for them.",
    heroHeading: "The Lighting Operator",
    heroSubheading:
      "Sets the mood of the room from the console — while WorshipMetrics keeps the rig documented, monitored, and connected to the rest of the service.",
    skillLevel: "Intermediate",
    typicalAge: "14+",
    roleSentence:
      "The Lighting Operator shapes the room: the looks, the transitions, and the moments where light helps the service feel intentional.",
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
      "The console stays the instrument — that's where the looks live. What WorshipMetrics adds is everything around it: the rig documented, the console monitored, and the service plan connected to the cues the operator fires.",
    controls: [
      "The lighting rig documented on the Signal Map — every fixture run, dimmer, and console connection labeled",
      "Factory port maps for common lighting consoles in the device catalog",
      "Console health on the AV monitoring dashboard, so a dead console is caught at sound check, not at the first song",
      "Present protocol presets that can fire OSC cues at consoles configured to listen for them",
      "The service plan alongside, so look changes land on the moment instead of a beat behind it",
    ],
    behavior:
      "The operator builds looks on the console the way the console intends. WorshipMetrics makes sure the next volunteer can find the rig's wiring, the team can see the console is healthy, and the cues have a plan to follow.",
    techReassurance:
      "The Signal Map, monitoring, and service plan run in any browser on a laptop, phone, or WorshipMetrics Tablet over the church Wi-Fi.",
    compatibilityIntro:
      "This role scales from a real console-driven rig down to simple room-light control.",
    compatibilityGroups: [
      {
        heading: "Works alongside major lighting environments",
        items: [
          "Consoles from MA Lighting, ChamSys, Avolites, and more documented in the device catalog with factory port maps",
          "OSC cues from Present for consoles that accept network triggers",
          "Churches without a full rig still get the serving structure, the plan, and a documented booth",
        ],
      },
    ],
    tabletBody:
      "A tablet is useful here because volunteers can walk the room during setup or rehearsal, check the plan, and judge the look from where people actually sit.",
    teamPlacement:
      "Lighting is a creative-track role. Volunteers who love it often stay in it for years and become the people who shape how the room feels.",
  },
  {
    slug: "recording-archivist",
    image: "/images/roles/av-role-recording-archivist.jpg",
    title: "Recording / Archivist",
    subtitle: "The Historian",
    accentColor: "#4A6B7A",
    oneLine: "Makes sure every service is captured and useful afterward.",
    metaTitle: "Recording / Archivist | The Historian",
    metaDescription:
      "The Recording / Archivist makes sure every service is captured cleanly — recording control for vMix and OBS, an automatic cloud archive, and clips ready for the week after.",
    heroHeading: "The Recording / Archivist",
    heroSubheading:
      "The insurance policy. Make sure every service is being recorded cleanly, confirm the archive has it, and clip the moments worth keeping.",
    skillLevel: "Beginner to intermediate",
    typicalAge: "13+",
    roleSentence:
      "The Recording / Archivist makes sure the service is actually being captured, archived, and handed off well for the week that follows.",
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
      "The Archivist's whole job is one question: is this actually being captured? Between recording control in the booth and an automatic cloud archive behind the stream, that answer is never more than a glance away.",
    controls: [
      "Start and stop recording in vMix and OBS — with remote control when the seat is covered from somewhere else",
      "Every streamed service records to the cloud automatically — up to 4 hours per service, kept for 120 days",
      "Frame-accurate clipping to pull the sermon or a worship moment out of the full recording",
      "Live clips up to 10 minutes long, captured before the service even ends",
      "HyperDeck recorder status monitored in the booth, so a full disk is caught before Sunday",
    ],
    behavior:
      "The archive happens automatically behind every streamed service, and the local recording is one confirmed click — so the answer to \"did we get it?\" is always yes, twice.",
    techReassurance:
      "The archive and clipping tools run in any browser. Local recording control runs through the booth's production computer.",
    compatibilityIntro:
      "This role bridges the live service and the week-after workflow, which makes it especially valuable for content-minded churches.",
    compatibilityGroups: [
      {
        heading: "Works with common recording paths",
        items: [
          "vMix and OBS recording workflows, locally and remotely",
          "The automatic cloud recording behind WorshipMetrics streaming, with 120-day retention",
          "Blackmagic HyperDeck status monitoring for churches recording to hardware",
          "The clip pipeline that turns the archive into sermon clips and social-ready Reels",
        ],
      },
    ],
    tabletBody:
      "A tablet lets this volunteer keep capture status, the plan, and the team chat in one place without demanding a full booth workstation.",
    teamPlacement:
      "Recording is a great entry seat for detail-oriented students and a strong support seat for veterans who want to serve without carrying the full live pressure of the Director chair.",
  },
];

export const avTeamHub = {
  title: "Build Your AV Team",
  heroHeading: "You don't need more gear. You need a team.",
  heroSubheading:
    "WorshipMetrics gives every church an AV Club out of the box: seven volunteer roles, a training path for each seat, and a structure that turns your media ministry into a thriving youth ministry.",
  metaDescription:
    "WorshipMetrics gives your church a complete AV team structure: seven volunteer roles, each with a clear job on Sunday, a training path, and a place on the team.",
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
