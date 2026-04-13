export type BrandCategory = 'camera' | 'switcher' | 'encoder' | 'mixer' | 'software';

export interface Brand {
  slug: string;
  name: string;
  category: BrandCategory[];
  origin: 'chinese-budget' | 'western-pro' | 'western-budget';
  pricePosition: 'budget' | 'mid' | 'pro';
  churchMarketShare: 'dominant' | 'high' | 'medium' | 'niche';
  description: string;
}

export const brands: Brand[] = [
  { slug: 'avkans', name: 'AVKANS', category: ['camera'], origin: 'chinese-budget', pricePosition: 'budget', churchMarketShare: 'high', description: 'Budget NDI PTZ cameras popular in small and medium churches.' },
  { slug: 'tenveo', name: 'Tenveo', category: ['camera'], origin: 'chinese-budget', pricePosition: 'budget', churchMarketShare: 'high', description: 'Affordable USB and HDMI PTZ cameras for church streaming setups.' },
  { slug: 'tongveo', name: 'TONGVEO', category: ['camera'], origin: 'chinese-budget', pricePosition: 'budget', churchMarketShare: 'medium', description: 'Budget PTZ cameras with NDI support for church environments.' },
  { slug: 'fomako', name: 'FoMaKo', category: ['camera'], origin: 'chinese-budget', pricePosition: 'budget', churchMarketShare: 'medium', description: 'Chinese-manufactured PTZ cameras with competitive price-to-feature ratio.' },
  { slug: 'smtav', name: 'SMTAV', category: ['camera'], origin: 'chinese-budget', pricePosition: 'budget', churchMarketShare: 'medium', description: 'NDI-capable PTZ cameras in the sub-$500 church camera segment.' },
  { slug: 'obsbot', name: 'OBSBOT', category: ['camera'], origin: 'chinese-budget', pricePosition: 'mid', churchMarketShare: 'medium', description: 'AI-powered PTZ cameras with auto-tracking, popular for smaller worship spaces.' },
  { slug: 'minrray', name: 'Minrray', category: ['camera'], origin: 'chinese-budget', pricePosition: 'mid', churchMarketShare: 'niche', description: 'Conference-grade PTZ cameras with solid IP and NDI support.' },
  { slug: 'blackmagic', name: 'Blackmagic Design', category: ['switcher', 'encoder'], origin: 'western-pro', pricePosition: 'mid', churchMarketShare: 'dominant', description: 'Maker of the ATEM Mini switcher line — the most popular church video switcher in the world.' },
  { slug: 'roland', name: 'Roland', category: ['switcher'], origin: 'western-pro', pricePosition: 'mid', churchMarketShare: 'high', description: 'Professional video mixer brand with growing church presence, known for the V-1HD.' },
  { slug: 'kiloview', name: 'Kiloview', category: ['switcher', 'encoder'], origin: 'chinese-budget', pricePosition: 'budget', churchMarketShare: 'medium', description: 'Budget-conscious HDMI/SDI-to-NDI encoders and decoders popular in cost-sensitive church installs.' },
  { slug: 'magewell', name: 'Magewell', category: ['encoder'], origin: 'western-pro', pricePosition: 'pro', churchMarketShare: 'high', description: 'Professional hardware encoders trusted in broadcast and larger church environments.' },
  { slug: 'teradek', name: 'Teradek', category: ['encoder'], origin: 'western-pro', pricePosition: 'pro', churchMarketShare: 'medium', description: 'Aspirational live production encoders used in growing churches and broadcast environments.' },
  { slug: 'epiphan', name: 'Epiphan', category: ['encoder'], origin: 'western-pro', pricePosition: 'pro', churchMarketShare: 'niche', description: 'Established hardware encoder brand with a loyal install base in medium and large churches.' },
  { slug: 'behringer', name: 'Behringer', category: ['mixer'], origin: 'western-budget', pricePosition: 'budget', churchMarketShare: 'dominant', description: 'Maker of the X32 — the most widely installed digital mixer in churches globally.' },
  { slug: 'allen-heath', name: 'Allen & Heath', category: ['mixer'], origin: 'western-pro', pricePosition: 'mid', churchMarketShare: 'high', description: 'Premium UK mixer brand with the SQ series gaining significant church install share.' },
  { slug: 'yamaha', name: 'Yamaha', category: ['mixer'], origin: 'western-pro', pricePosition: 'mid', churchMarketShare: 'high', description: 'Established mixer brand with the TF series widely used in small-medium churches.' },
  { slug: 'mackie', name: 'Mackie', category: ['mixer'], origin: 'western-budget', pricePosition: 'budget', churchMarketShare: 'medium', description: 'Budget-friendly mixer brand with the DL32R popular in tablet-controlled church setups.' },
  { slug: 'presonus', name: 'PreSonus', category: ['mixer'], origin: 'western-pro', pricePosition: 'mid', churchMarketShare: 'medium', description: 'Digital mixer brand with the StudioLive series used in serious church production setups.' },
];

export const brandMap = Object.fromEntries(brands.map(b => [b.slug, b]));
