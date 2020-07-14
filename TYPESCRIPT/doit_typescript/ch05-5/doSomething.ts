import { ResultType } from './ResultType';

export const doSomething = (): ResultType => {
  try {
    throw new Error('Some Error occurs...');
  } catch (e) {
    return [false, e.message];
  }
};
