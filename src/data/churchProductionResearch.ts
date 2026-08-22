/**
 * Findings from Church Production Magazine's "Then vs. Now" research series,
 * published June 2026. Every number here is quoted from the published survey —
 * keep the citation attached wherever these appear.
 *
 * Note: the published cross-tabs for reliability and cost/value in the
 * under-500 column are internally inconsistent with the article's own summary,
 * so they are deliberately not reproduced here. Only headline figures and the
 * cross-tabs that match the narrative are included.
 */

export const researchSource = {
  publication: "Church Production Magazine",
  title: "Then vs. Now: How Church Production Is Shifting",
  detail: "Research Series, June 2026",
};

export const researchCitation = `Source: ${researchSource.publication}, “${researchSource.title},” ${researchSource.detail}.`;

export type ResearchStat = {
  stat: string;
  label: string;
};

/** Training has overtaken recruitment as the hardest part of running a team. */
export const trainingStats: ResearchStat[] = [
  { stat: "57%", label: "call training and skill development their top operational challenge — up 20 points, now ahead of volunteer recruitment" },
  { stat: "76%", label: "name volunteer training a production priority, up from 52% two years ago" },
  { stat: "72%", label: "run production mostly on volunteers — and 79% at churches under 500" },
];

/** Recruitment is hard, and hardest for the churches with the least help. */
export const recruitmentStats: ResearchStat[] = [
  { stat: "75%", label: "of small churches find volunteer recruitment at least somewhat difficult" },
  { stat: "7%", label: "of small churches call recruitment easy" },
  { stat: "72%", label: "of all churches now run production mostly on volunteers, up 7 points" },
];

/** Buyers stopped leading with price. */
export const buyingStats: ResearchStat[] = [
  { stat: "73%", label: "weigh reliability when evaluating technology — up 23 points, now the leading criterion" },
  { stat: "65%", label: "weigh ease of use for volunteers, up 15 points" },
  { stat: "#3", label: "where cost now ranks. Two years ago it was the number one criterion" },
];

/** Systems got more complex faster than teams could absorb. */
export const complexityStats: ResearchStat[] = [
  { stat: "+15pp", label: "growth in churches naming system complexity a core operational challenge, now 38%" },
  { stat: "+23pp", label: "growth in networking and infrastructure as a production priority, now 64%" },
  { stat: "27%", label: "now report higher expectations from church leadership, nearly double two years ago" },
];

/** The case for integrating rather than adding another system. */
export const integrationStats: ResearchStat[] = [
  { stat: "48%", label: "weigh integration with existing systems when buying — nearly double two years ago" },
  { stat: "38%", label: "name system complexity a core operational challenge, up 15 points" },
];

/** Short-form content went from niche to expected. */
export const contentStats: ResearchStat[] = [
  { stat: "60%", label: "name content creation a production priority — double the 30% of two years ago, the single biggest mover in the survey" },
  { stat: "80%", label: "of churches over 1,000 now treat it as a priority" },
  { stat: "81%", label: "name streaming and broadcast a priority, holding at already-high levels" },
];
